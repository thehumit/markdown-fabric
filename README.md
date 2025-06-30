# markdown-fabric

Шаблон-репозиторий для удобной работы с markdown, PlantUML и Mermaid.

## Как начать

1. Установите зависимости для генерации диаграмм:
   ```bash
   sudo apt-get update && sudo apt-get install -y plantuml
   npm install -g @mermaid-js/mermaid-cli
   ```
2. Поместите диаграммы в каталог `docs/diagrams`.
3. Запустите `scripts/render_diagrams.sh`, чтобы сгенерировать изображения в `docs/generated`.
   Каталог `docs/generated` добавлен в `.gitignore`, поэтому готовые картинки не
   хранятся в репозитории.
   Скрипт использует `scripts/puppeteer.json` для запуска `mmdc` без sandbox,
   что упрощает работу в root-окружениях.
