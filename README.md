# MCP Installer

원클릭으로 Stitch MCP와 NotebookLM MCP를 설치하는 웹 인터페이스입니다.

## 🚀 빠른 시작

### 웹에서 설치하기

1. [MCP Installer 웹사이트](https://tskim81.github.io/mcp-installer) 방문
2. Install 버튼 클릭
3. 터미널에 복사된 명령어 붙여넣기

### 직접 설치하기

터미널에서 다음 명령어를 실행하세요:

```bash
curl -fsSL https://raw.githubusercontent.com/tskim81/mcp-installer/main/install.sh | bash
```

## 📦 설치되는 항목

- **Stitch MCP**: Google의 UI 디자인 도구
- **NotebookLM MCP**: Google의 AI 노트 정리 도구
- **설정 파일**: `~/.gemini/antigravity/` 경로에 자동 설치

## 🛠️ 설치 경로

```
~/.gemini/antigravity/
├── mcp_config.json          # MCP 설정 파일
└── stitch_proxy.py          # Stitch MCP 프록시
```

## 📋 요구사항

- macOS
- Python 3
- 인터넷 연결

## 🔧 수동 설정

설치 스크립트가 자동으로 다음을 수행합니다:

1. `uv` (Python 패키지 매니저) 설치
2. NotebookLM MCP 서버 설치
3. Stitch MCP 프록시 다운로드
4. 설정 파일 다운로드 및 배치

## 📝 라이선스

MIT License

## 👤 작성자

Created by Jay @ Connect AI LAB
