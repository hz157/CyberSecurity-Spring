<!--
 * @Descripttion: 
 * @version: 
 * @Author: Ryan Zhang (gitHub.com/hz157)
 * @Date: 2024-03-23 23:21:40
 * @LastEditors: Ryan Zhang
 * @LastEditTime: 2024-03-23 23:25:25
-->
# PDF-XSS 

> 请在授权环境下进行渗透测试!!!

## 漏洞介绍
PDF-XSS（PDF跨站脚本攻击）漏洞是一种安全漏洞，通常出现在网页中嵌入的PDF文档中。当用户打开包含恶意JavaScript代码的PDF文件时，这些代码会在用户的浏览器中执行，从而可能导致跨站脚本攻击。

攻击者利用PDF-XSS漏洞，可以通过在PDF文件中注入恶意的JavaScript代码，来执行各种恶意操作，例如窃取用户的敏感信息、在用户浏览器中执行未经授权的操作等。这种攻击对用户的影响可能非常严重，因为PDF文件通常被认为是相对安全的文件格式，用户可能会轻易地打开包含恶意代码的PDF文件而不加以怀疑。

## 如何使用
### 1. 有Goland的环境下
```
go mod tidy
go run pdf-xss.pdf
```
### 2.无Goland环境
下载pdf-xss.exe 直接运行，输入alert内容后会在exe根目录下生成一个pdf-xss.pdf的文件，该文件内存在javascript alert代码。


## 防范措施
为了防止PDF-XSS漏洞，用户和开发者需要采取一些措施，包括：不轻易打开来自不可信来源的PDF文件、使用安全的PDF阅读器、及时更新PDF阅读器软件、避免在网页中直接嵌入PDF文档等。同时，开发者还需要注意在生成PDF文件时，避免将用户提供的数据直接插入到PDF文档中，以防止注入恶意代码。