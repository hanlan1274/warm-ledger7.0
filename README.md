# 暖账 0.2.3 · 新仓库首次构建

1. 将本ZIP解压后的全部内容上传到新GitHub仓库根目录，包含.github。
2. Actions → Build Android APK → Run workflow，保持first_build已勾选，直接运行。首次无需添加签名Secrets。
3. 成功后在本次运行Artifacts下载warm-ledger-0.2.3-apk，解压安装APK。
4. 同时下载并妥善保存warm-ledger-signing-backup-KEEP-PRIVATE，供未来更新使用，勿上传仓库。

本包保留全部最新功能：计划外支出、代管承担金额、收入补回、负余额快照修复。版本0.2.3。
全新签名通常不能覆盖旧签名App。旧App先导出完整备份，必要时卸载后安装新版并导入备份。
本包为首次构建配置。首次成功后，未来更新请设置签名备份中的两个Secrets，并取消first_build。
源码已通过50项Flutter测试和20项模型回归；APK仍需由GitHub Actions实际编译。
