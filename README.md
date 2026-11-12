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


## 자동 배포

`main` 브랜치에 변경 사항이 푸시되면, GitHub Actions 워크플로(`.github/workflows/publish.yml`)가 자동으로 `mybook`의 내용을 빌드하여 `gh-pages` 브랜치로 게시합니다.

