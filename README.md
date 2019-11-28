# BrandSiHai
This is a quickAPP centered on Brand.


## Server
- `docker build -t 'brandsihai' . `  build docker image
- `docker run -it --rm -p 7001:7001  -v /home/ftp/BrandSiHai:/Project/demo brandsihai`  run image on port 7001 ,and mount your directory to docker file system (so that model.tar can be access)
- `localhost:7001/test`  access address on browser
- `http://139.9.124.104:7001/test`  remote backend api 

## Quick App
- 安卓客户端 。 快应用资源下载页面 ，下载 [快应用调试器](https://www.quickapp.cn/docCenter/post/69) ，安装
- Github 项目 **/quickapp/dist**  下载导出的 **.rpk** 包，使用 **快应用调试器** 安装
- 运行并测试

![运行示例](snapshot⁩/howtouse.gif)
