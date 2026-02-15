function showStatus(message, type) {
    const statusDiv = document.getElementById('status');
    statusDiv.innerHTML = message.replace(/\n/g, '<br>');
    statusDiv.className = `status ${type}`;

    // Don't auto-hide for success messages
    if (type !== 'success') {
        setTimeout(() => {
            statusDiv.style.display = 'none';
        }, 5000);
    }
}

function showInstallInstructions(mcpName) {
    const installCommand = 'curl -fsSL https://raw.githubusercontent.com/tskim81/mcp-installer/main/install.sh | bash';

    showStatus(`${mcpName} 설치를 시작합니다...`, 'info');

    // Copy to clipboard
    navigator.clipboard.writeText(installCommand).then(() => {
        const message = `
<strong>✅ 설치 명령어가 클립보드에 복사되었습니다!</strong><br><br>
터미널에서 다음 명령어를 실행하세요:<br>
<code>${installCommand}</code><br><br>
또는 복사된 명령어를 터미널에 붙여넣기(Cmd+V) 하세요.<br><br>
<strong>이 명령어는 다음을 자동으로 설치합니다:</strong><br>
• Stitch MCP<br>
• NotebookLM MCP<br>
• PayPal MCP (설정 필요)<br>
• Firebase MCP<br>
• 설정 파일 (~/.gemini/antigravity/)
        `.trim();

        showStatus(message, 'success');
    }).catch(() => {
        showStatus(`설치 명령어: ${installCommand}`, 'info');
    });
}

function installStitch() {
    showInstallInstructions('Stitch MCP');
}

function installNotebookLM() {
    showInstallInstructions('NotebookLM MCP');
}

function installPayPal() {
    showInstallInstructions('PayPal MCP');
}

function installFirebase() {
    showInstallInstructions('Firebase MCP');
}

// 페이지 로드 시 환영 메시지
window.addEventListener('load', () => {
    console.log('MCP Installer loaded successfully!');
});
