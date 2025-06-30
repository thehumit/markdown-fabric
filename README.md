# markdown-fabric

Шаблон-репозиторий для удобной работы с markdown, PlantUML и Mermaid.

## Как начать

1. Установите зависимости для генерации диаграмм. На Linux используйте:
   ```bash
   sudo apt-get update && sudo apt-get install -y plantuml
   npm install -g @mermaid-js/mermaid-cli
   ```
   На macOS те же инструменты можно установить через Homebrew:
   ```bash
   brew install plantuml node
   npm install -g @mermaid-js/mermaid-cli
   ```
2. Поместите диаграммы в каталог `docs/diagrams`.
3. Сгенерируйте изображения одним из скриптов:
   - `scripts/render_diagrams.sh` – bash-версия.
   - `scripts/render_diagrams.py` – кроссплатформенная альтернатива на Python.
   Файлы появятся в каталоге `docs/generated`, который исключён из репозитория.
   Скрипты используют `scripts/puppeteer.json` для запуска `mmdc` без sandbox,
   что упрощает работу в root-окружениях.
