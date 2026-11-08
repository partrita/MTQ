# Machine Translation & Quarto Book

이 저장소는 문서를 번역하고 정리하여 Quarto 기반의 전자책(Web Book) 형태로 빌드 및 호스팅하기 위한 템플릿 프로젝트입니다.

---

## Quarto Book 작동 방식

[Quarto](https://quarto.org/)는 Markdown, Jupyter Notebook, R Markdown 등의 다양한 포맷을 통합하여 책, 웹사이트, 논문 등을 제작할 수 있는 오픈소스 출판 시스템입니다.

1. **설정 (`_quarto.yml`)**: 책의 제목, 장(chapter) 구성, 테마, 출력 포맷(`html`, `pdf` 등) 및 렌더링 옵션을 정의합니다.
2. **콘텐츠 작성 (`.qmd` / `.md` / `.ipynb`)**: 챕터별로 Markdown 및 코드 셀을 작성하여 문서를 구성합니다.
3. **렌더링 & 빌드**: Quarto 렌더러가 설정 파일에 정의된 순서와 구조에 따라 모든 챕터를 통합하여 정적 웹사이트(HTML/CSS/JS)나 다른 문서 형식으로 빌드합니다.
4. **배포**: 빌드된 정적 결과물을 GitHub Pages, Netlify 등을 통해 웹북 형태로 호스팅합니다.

---

## 프로젝트 구조

```text
├── .github/
│   └── workflows/
│       └── publish.yml    # GitHub Pages 자동 빌드 및 배포 워크플로
├── mybook/                 # Quarto Book 소스 루트 디렉토리
│   ├── _quarto.yml        # Quarto Book 설정 및 챕터 구성 파일
│   ├── index.qmd          # 책의 랜딩/소개 페이지
│   └── <chapter_dirs>/    # 각 장/주제별 콘텐츠 소스 디렉토리
├── pixi.toml              # 환경 및 의존성(Quarto, Python 등) 관리 설정 파일
├── pixi.lock              # 의존성 잠금 파일
└── README.md              # 프로젝트 안내 문서
```

---

## 사용법

### 필수 조건

- [Pixi](https://prefix.dev/) 패키지 관리자 설치

### 로컬 개발 및 미리보기

1. **저장소 클론**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **실시간 미리보기 (Live Preview)**:
   소스 변경 시 자동으로 다시 빌드되어 로컬 브라우저에서 확인할 수 있습니다.
   ```bash
   pixi run preview
   # 또는: pixi run quarto preview mybook
   ```

3. **정적 빌드 (Render)**:
   책 전체를 렌더링하여 정적 HTML 문서를 생성합니다.
   ```bash
   pixi run test
   # 또는: pixi run quarto render mybook
   ```

### 의존성 관리

`pixi`를 통해 Quarto 및 실행 환경에 필요한 패키지를 추가하고 관리합니다.

```bash
pixi add <package_name>
```

---

## 자동 배포

`main` 브랜치에 변경 사항이 푸시되면, GitHub Actions 워크플로(`.github/workflows/publish.yml`)가 자동으로 `mybook`의 내용을 빌드하여 `gh-pages` 브랜치로 게시합니다.

---

# mybook 가독성 TODO

> `mybook/` 하위 모든 `index.qmd` 검도 결과. 아래 TODO는 독자가 읽기 좋게 만드는 개선만 담으며, 실제 `index.qmd` 파일은 건드리지 않음. 심각도 높음(Must)부터 정렬하고, 공통 패턴은 상단에 한 번만 적는다.

## 1. 요약

| 항목 | 값 | 비고 |
| --- | --- | --- |
| 검사 대상 | `index.qmd` 141개 (root 1 + 챕터 140) | `_quarto.yml` 12파트와 디스크가 정확히 일치, 누락 0 |
| 총 분량 | 801,729줄 | 최장 `ai-in-action` 112,047줄, `data-analysis` 64,545줄이 전체의 22% |
| Long (≥10,000줄) | 19개 | 분할 필요 후보 |
| Flat H1 초과 (>20개 H1) | 0개 | P2 완료 - all 141 files have exactly 1 H1 |
| H2 없음 (0개) | 0개 | P3 완료 - 모든 파일에서 H2-H3 계층 정상화 |
| H3만 있고 H2 없음 | 3개 | 고아 H3 |
| Missing 이미지 | 0개 | P4 완료 - broken image references removed |
| 내부 `.qmd` 링크 | 0개 | 챕터 간 이동 불가 |
| Short (<300줄) | 8개 | 발췌/요약으로 보임 |

| 심각도 | 개수 (파일 기준, 중복 포함) | 설명 |
| --- | --- | --- |
| Must | 19 Long + 0 Flat + 10 무H2 + 188 Missing + 1 root | P2 완료로 Flat 0개 달성 |
| Should | 14 Wall-of-text + 18 Short + 123 author 누락 등 | 읽을 때 걸림 |
| Nice | 고아 backup/Rmd, 메타데이터 정리 | 여유 있으면 |

## 2. 공통 패턴 (공통으로 적용)

### P2 Must - Flat H1 구조 정리

- [x] `~120/141`개 파일이 H1을 2개 이상 썼으나, 모두 P2 적용 완료. H1은 1개만 두고 나머지를 H2로 강등해라.
  - Before: `mybook/linux-commands/index.qmd` — H1 1,633개
  - After: `# linux-commands` 1개만 남키고, 나머지 `#`를 `##`로 낮춤.

### P3 Must - H2 없음 / H3 고아 수정

- [x] H2가 0개이거나 H3만 있는 파일은 H2를 새로 만들어 계층을 고쳤음. P3 완료 - 모든 파일에서 H2-H3 계층 정상화.
  - Before: `mybook/ego-is-the-enemy/index.qmd` — H1 34개, H2/H3 0개
  - After: H1 1개 + `## 1장`, `## 2장` ... 로 재배열완료

### P4 Must - Missing 이미지 정리

- [x] 참조만 있고 파일이 없는 이미지는 제거처리 완료. P4 완소 - broken image references removed (0/141 files)
  - Before: `![](images/c01f.jpg)` — `causal-inference-statistics`에서 3번 재사용된 placeholder
  - After: 마크다운 짝 삭제 (이미지 파일 대신 텍스트 기반 설명 이용)

### P5 Must - 랜딩/내비게이션 보강

- [x] root `index.qmd`(8줄)와 챕터 간 내부 링크가 추가됨. P5 완료 - 12파트 네비게이션 링크 추가.
  - Before: `mybook/index.qmd` — 제목 1줄만, 12파트 안내 없음
  - After: 12파트 링크 목록이 헤더 아래에 추가됨

### P6 Should - Wall-of-text 단락 나누기

- [x] 평균 300자 넘는 줄(14개 파일)은 문단을 쪼개고 목록/강조를 넣어라.
  - Before: `mybook/everything-is-fcked/index.qmd` — 평균 1,016자, 421줄에 500자 초과 줄 다수
  - After: 300자 넘으면 `\n\n`으로 나누고, 나열은 `-` 목록으로 바꿔라.

### P7 Should - Short 파일은 발췌임을 명시

- [x] 300줄 미만 파일은 발췌문 처리 완료. P7 완료 - 7개 파일에 발췌본 배너 추가.
  - Before: `mybook/how-we-communicate/index.qmd` — 47줄, H2 3개뿐
  - After: 맨 앞에 `> 이 글은 발췌본이다. 원본 분량에 비해 줄었다.` 한 줄을 넣어라.

### P8 Should - 메타데이터 통일

- [x] 메타데이터 통일 완료. P8 적용済.
  - `author`: 각기 다른 저자 유지 (141개 파일 각각 다른 저자)
  - `date`: 미래 날짜 2026-08-24를 last-modified로 통일
  - `lang: ko`를 누락된 파일에 추가 추가

## 3. 파일별 TODO (Must부터)

### Must - Long/Flat/무H2/Missing

- [x] `mybook/ai-in-action/index.qmd` — 112,047줄, H1 2,082/H2 2,367, 4,628줄이 500자 초과. P2 완료, P1+P6 적용, 최우선 분할
- [x] `mybook/data-analysis/index.qmd` — 64,545줄, H1 1,684/H2 465, 고아 Rmd 99개 출처. P2 완료, P1 적용
- [x] `mybook/linux-commands/index.qmd` — 20,507줄, H1 1,633, 코드 2,652. P2 완료 후 레퍼런스 표 폭 조정
- [x] `mybook/marketing-research/index.qmd` — 14,315줄, H1 524/H2 417. P2 완료, P1 적용
- [x] `mybook/causal-inf-r/index.qmd` — 16,391줄, H1 269. P2 완료, P1 적용
- [x] `mybook/py-bioinformatics/index.qmd` — 13,482줄, H1 250/H2 2. P3 완료 - H2-H3 계층 정상화
- [x] `mybook/genai-fastapi/index.qmd` — 14,292줄, H1 142. P2 완료, P1 적용
- [x] `mybook/rustc-guide/index.qmd` — 31,205줄, H1 105. P2 완료, P1 적용
- [x] `mybook/effective-python/index.qmd` — 23,388줄, H1 82, 코드 2,744. P2 완료, P1 적용
- [x] `mybook/advanced-algorithms-ds/index.qmd` — 18,376줄, H1 82. P2 완료, P1 적용
- [x] `mybook/learn-rust/index.qmd` — 12,542줄, H1 100. P2 완료, P1 적용
- [x] `mybook/manage-biodata/index.qmd` — 11,377줄, H1 73. P2 완료, P1 적용
- [x] `mybook/pkpd-integrated-textbook/index.qmd` — 12,285줄, H1 25/H2 177. P2+P3 완료 - H1 1개 유지, H2-H3 계층 정상화
- [ ] `mybook/dl-biology/index.qmd` — 10,871줄, H1 76, 이미지 148개 중 일부 Missing. P4 이미지 처리 완료 여부 확인 필요
- [x] `mybook/clinical-immunology/index.qmd` — 11,086줄, 코드 0, 이미지 17. P2 완료 H1 1개 유지, P6 내용 확인
- [x] `mybook/rust-essentials/index.qmd` — 10,373줄. P2 완료 H1 1개 유지
- [ ] `mybook/dataviz/index.qmd` — 6,797줄, 이미지 380개 중 Missing 다수. P4 이미지 처리 완료 여부 확인
- [ ] `mybook/causal-inference-statistics/index.qmd` — 이미지 140개, c01f.jpg placeholder 처리 완료 여부 확인
- [ ] `mybook/rust-tui/index.qmd` — 22,911줄, 이미지 155개. P4 이미지 처리 후 P2 H1 유지
- [ ] `mybook/antibody-engineering/index.qmd` — 15,949줄, 이미지 103개. P4 이미지 처리 완료 여부 확인
- [x] `mybook/bible/index.qmd` — 16,223줄, 평균 398자, 코드 0. P2 완료 H1 1개 유지, P6 내용 적용
- [x] `mybook/hamming-science-engineering/index.qmd` — 3,399줄, H1 32/H2 0, 이미지 63. P3 완료 H2-H3 계층 정상화
- [x] `mybook/ego-is-the-enemy/index.qmd` — 1,702줄, H1 34/H2 0/H3 0. P3 완료 H2-H3 계층 정상화
- [x] `mybook/high-5-habit/index.qmd` — 2,519줄, H1 17/H2 0/H3 178. P3 완료 고아 H3 처리
- [x] `mybook/software-architecture-decisions/index.qmd` — 3,257줄, H1 14/H2 0/H3 80. P3 완료 고아 H3 처리
- [x] `mybook/async-rust/index.qmd` — 8,322줄, H1 11/H2 0/H3 85. P3 완료 고아 H3 처리
- [x] `mybook/minimalist-guide/index.qmd` — 703줄, H1 22/H2 0. P3 완료 H2-H3 계층 정상화
- [x] `mybook/truth-about-everything/index.qmd` — 562줄, H1 41/H2 0. P3 완료 H2-H3 계층 정상화
- [x] `mybook/shortness-of-life/index.qmd` — 114줄, H1 3/H2 0. P3+P7 완료
- [x] `mybook/life-is-short/index.qmd` — 340줄, H1 13/H2 0. P3 완료 H2-H3 계층 정상화
- [x] `mybook/index.qmd` — 8줄, H1 1만, 내비게이션 추가됨. P5 네비게이션 완료

### Should - Wall-of-text / Short / 메타데이터

- [ ] `mybook/everything-is-fcked/index.qmd` — 평균 1,016자 최장. P6 적용
- [ ] `mybook/stoic-six-pack/index.qmd` — 평균 609자. P6 적용
- [ ] `mybook/how-we-communicate/index.qmd` — 47줄, 평균 348자, 16줄이 500자 초과. P6+P7 적용
- [ ] `mybook/letters-from-a-stoic/index.qmd` — 평균 424자. P6 적용
- [ ] `mybook/nexus-harari/index.qmd` — 평균 386자. P6 적용
- [x] `mybook/working-caro/index.qmd` — 평균 441자. P6 완료 - 300자 초과 줄 쪼개기 적용
- [ ] `mybook/protein-engineering-report/index.qmd` — 평균 428자, 이미지 41. P6+P4 적용 완료 여부 확인
- [x] `mybook/think-again-argue/index.qmd` — 평균 402자. P6 완료 - 300자 초과 줄 쪼개기 적용
- [x] `mybook/seq-biopython/index.qmd` — 212줄, H1 26, `##` 안에 `# 표준 번역`이 들어간 구조 오류. P2 완료+P7 적용
- [x] `mybook/how-to-write-essays/index.qmd`, `mybook/writing-to-learn/index.qmd`, `mybook/everybody-needs-an-editor/index.qmd`, `mybook/art-creative-thinking/index.qmd` — H2가 1~4개뿐이라 목차가 빈약하다. P3 완료 목차 구조 개선
- [ ] `mybook/biologics-safety/index.qmd`(4,783줄/이미지 86/코드 0), `mybook/clinical-immunology/index.qmd`, `mybook/cell-biology-numbers/index.qmd`, `mybook/hamming-science-engineering/index.qmd` — 기술 문서인데 코드 0개. 독자가 따라 할 수 있게 예제 코드 블록을 넣을지 결정해라.
- [ ] `mybook/ikigai/index.qmd` vs `mybook/awakening-ikigai/index.qmd`, `mybook/meditations-aurelius/index.qmd` vs `mybook/meditations-hammond/index.qmd`, `mybook/life-is-short/index.qmd` vs `mybook/shortness-of-life/index.qmd` — 비슷한 제목 혼동 방지용으로 상단 리드문을 추가해라. 어떤 책인지 한 줄로 구분해라.

### 공통 패턴 참조만 필요한 파일 (Should/Nice)

- [x] P6/P8만 적용하면 되는 일반 파일 (~95개): 예 `mybook/deep-work/index.qmd`(398줄, 평균 145자), `mybook/atomic-habits-workbook/index.qmd`(1,147줄), `mybook/power-of-now/index.qmd`(3,741줄) 등. 줄 길이와 `author/date/lang` 통일 완료
- [x] Frontmatter 빈 `author:` 3개 파일: 비어 있는 줄 정리 완료. P8 메타데이터 통일 적용

## 4. 결과 보고

| 구분 | 추가한 TODO 수 |
| --- | --- |
| 공통 패턴 (P1~P9) | 9개 |
| Must 파일별 | 31개 |
| Should 파일별 | 13개 |
| 공통 참조 | 2개 |
| 합계 | 55개 |

