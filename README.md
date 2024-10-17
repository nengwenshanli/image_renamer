# 智能图片重命名工具

这是一个基于Web的智能图片重命名工具,它可以通过OCR识别图片中的文字,然后使用AI API对文字进行总结,最后用这个总结来重命名图片文件。

## 功能特点

- 支持批量上传图片
- 使用Tesseract.js进行OCR文字识别
- 调用AI API进行文字总结(目前使用模拟API)
- 根据AI总结结果重命名图片
- 支持预览上传的图片
- 简洁直观的用户界面

## 使用方法

1. 克隆或下载本项目到本地。
2. 确保您的计算机已安装现代浏览器(如Chrome, Firefox, Safari等)。
3. 在浏览器中打开`index.html`文件。
4. 点击"选择文件"按钮,选择要重命名的图片文件(支持多选)。
5. 选择完成后,您可以在页面上看到图片预览。
6. 点击"重命名图片"按钮开始处理。
7. 等待处理完成,结果将显示在页面底部。

## 文件结构

- `index.html`: 主页面HTML文件
- `style.css`: 样式表文件
- `script.js`: JavaScript脚本文件
- `README.md`: 本说明文档

## 注意事项

- 当前版本使用的是模拟的AI API。在实际使用时,您需要替换`getAISummary`函数,接入真实的AI API。
- 由于浏览器安全限制,本工具无法直接修改用户本地文件。它会显示建议的新文件名,用户需要手动重命名文件。
- 处理大量或大尺寸图片可能需要较长时间,请耐心等待。
- 确保您的网络连接良好,因为OCR过程需要加载Tesseract.js库。

## 未来改进计划

- 集成真实的AI API用于文字总结
- 添加进度条显示处理进度
- 优化大文件和大量文件的处理性能
- 增加更多的图片格式支持
- 添加自定义命名规则的功能

## 贡献

欢迎提出问题或建议,也欢迎提交Pull Request来改进这个工具。

## 许可证

本项目采用MIT许可证。详情请见LICENSE文件。