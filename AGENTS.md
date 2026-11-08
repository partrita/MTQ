# Critical Constraints for Agents

## Project Overview
- **Purpose**: Document translation and publication as a Quarto-based Web Book.
- **Source Root**: `mybook/`
- **Configuration**: `mybook/_quarto.yml` (book structure, chapters, metadata)
- **Environment & Dependency**: Managed via `pixi` (`pixi.toml`)
- 파이썬 스크립트 실행시 'pixi run python' 사용

## Key Commands
- **Preview (Live Server)**: `pixi run preview` (or `pixi run quarto preview mybook`)
- **Build / Render**: `pixi run test` (or `pixi run quarto render mybook`)
- **Add Dependency**: `pixi add <package_name>`

## Conventions & Rules for AI Agents
1. **Book Structure**: When adding new chapters or documents, update `mybook/_quarto.yml` under `chapters` or `sidebar`.
2. **Content Files**: Place source content (`.qmd`, `.md`, `.ipynb`) inside `mybook/`.
3. **Validation**: Run `pixi run test` (quarto render) to verify builds before finalizing document edits.
3. 초대형 단일 페이지 `.qmd`로 생성 

## 에이전트가 자주 하는 실수 (반드시 방지)
1. pip 사용 (WRONG)
2. python3 사용 (WRONG)

