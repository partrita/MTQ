"""각 qmd를 같은 폴더의 txt로 변환하고, qmd에 TXT 다운로드 링크를 주입한다.

- stdlib만 사용. `pixi run python mybook/qmd_to_txt.py` 로 실행.
- 이미지 제거, 마크다운 가독 형식 유지. Div 마커(`:::`) 제거.
- 다운로드 링크는 Quarto `resources` + 상대경로 링크 사용 (출력 HTML에 txt 복사됨).
- Idempotent: 재실행해도 diff 없음.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MARKER = "<!-- txt-download -->"
SKIP_DIRS = {"docs", "_freeze", ".quarto", "site_libs"}

IMG_MD = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
HTML_IMG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
DIV_MARK = re.compile(r"^:::\s*(\{[^}]*\})?\s*$", re.MULTILINE)
SHORTCODE = re.compile(r"\{\{<[^>]*>\}\}")


def split_front_matter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[: end + 4], text[end + 4 :]
    return "", text


def qmd_to_txt(text):
    fm, body = split_front_matter(text)
    # 주입한 다운로드 블록은 txt에서 제외 (자기참조 방지)
    marker_at = body.find(MARKER)
    if marker_at != -1:
        body = body[:marker_at]
    title = ""
    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if m:
        title = m.group(1).strip()

    def img_sub(mo):
        alt = mo.group(1).strip()
        return f"[그림: {alt}]" if alt else ""

    body = IMG_MD.sub(img_sub, body)
    body = HTML_IMG.sub("", body)
    body = DIV_MARK.sub("", body)
    body = SHORTCODE.sub("", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    if title:
        body = f"# {title}\n\n" + body
    return body


def ensure_download_link(qmd: Path, txt_name: str):
    """qmd에 resources + 다운로드 블록 주입. 변경했으면 True."""
    text = qmd.read_text(encoding="utf-8")
    changed = False
    if MARKER not in text:
        block = (
            f"\n{MARKER}\n::: {{.callout-tip title=\"전자책용 TXT\"}}\n"
            f"[TXT 다운로드]({txt_name}){{download=\"{txt_name}\"}}\n:::\n"
        )
        text = text.rstrip("\n") + "\n" + block
        changed = True
    fm, body = split_front_matter(text)
    if txt_name not in fm:
        if re.search(r"^resources:\s*$", fm, re.MULTILINE):
            fm = re.sub(
                r"(?m)^resources:\s*$",
                f"resources:\n- {txt_name}",
                fm,
                count=1,
            )
        else:
            fm = fm[:-3].rstrip() + f"\nresources:\n- {txt_name}\n---\n"
        text = fm + body
        changed = True
    if changed:
        qmd.write_text(text, encoding="utf-8")
    return changed


def iter_qmds():
    for q in sorted(ROOT.rglob("*.qmd")):
        if any(part in SKIP_DIRS or part.endswith("_files") for part in q.parts):
            continue
        yield q


def main():
    n_txt = n_qmd = 0
    for qmd in iter_qmds():
        txt = qmd.with_name(qmd.stem + ".txt")
        converted = qmd_to_txt(qmd.read_text(encoding="utf-8"))
        if not txt.exists() or txt.read_text(encoding="utf-8") != converted:
            txt.write_text(converted, encoding="utf-8")
            n_txt += 1
        if ensure_download_link(qmd, txt.name):
            n_qmd += 1
    print(f"txt updated: {n_txt}, qmd link injected: {n_qmd}")


def self_check():
    src = '---\ntitle: "T"\n---\n\n# H\n\n![캡션](images/a.png)\n\n![](b.png)\n\n::: {.callout-note}\n내용\n:::\n'
    out = qmd_to_txt(src)
    assert "images/a.png" not in out and "<img" not in out, out
    assert "[그림: 캡션]" in out, out
    assert "\n:::" not in out, out
    assert out.startswith("# T\n"), out
    # 주입 블록은 txt에 안 들어감
    assert "TXT 다운로드" not in qmd_to_txt(src + f"\n{MARKER}\n[TXT 다운로드](index.txt)\n"), out
    print("self-check ok")


if __name__ == "__main__":
    if "--check" in sys.argv:
        self_check()
    else:
        main()
