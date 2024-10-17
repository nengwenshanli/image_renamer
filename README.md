# 智能图片重命名工具

这是一个基于Python的智能图片重命名工具，它可以通过OCR识别图片中的文字，然后使用AI API对文字进行总结，最后用这个总结来重命名图片文件。

## 功能特点

- 支持批量处理图片文件（格式：PNG, JPG, JPEG, GIF, BMP）。
- 使用EasyOCR进行OCR文字识别。
- 调用DeepSeek AI API进行文字总结。
- 根据AI总结结果（20个字以内）重命名图片文件。
- 简洁直观的用户界面。

## 使用方法

1. 克隆或下载本项目到本地。
2. 确保您的计算机已安装Python和所需的库：
   ```bash
   pip install easyocr Pillow requests numpy
   ```
3. 运行脚本：
   ```bash
   python image_renamer.py
   ```
4. 选择包含图像文件的文件夹。
5. 程序将处理文件并输出重命名结果。

## 注意事项

- 请确保您的API密钥有效，并替换代码中的`api_key`变量。
- 处理过程中可能会遇到OCR或API请求失败的情况，程序会自动跳过这些文件。
- 处理大量或大尺寸图片可能需要较长时间，请耐心等待。

## 未来改进计划

- 集成更多的AI API用于文字总结。
- 添加进度条显示处理进度。
- 优化大文件和大量文件的处理性能。
- 增加更多的图片格式支持。
- 添加自定义命名规则的功能。

## 贡献

欢迎提出问题或建议，也欢迎提交Pull Request来改进这个工具。

## 许可证

本项目采用MIT许可证。详情请见LICENSE文件。
```
