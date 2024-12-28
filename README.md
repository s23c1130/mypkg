<!---
  SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
  SPDX-License-Identifier:BSD-3-Clause
--->

[![test](https://github.com/s23c1130/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/s23c1130/mypkg/actions/workflows/test.yml)

# はじめに
マウスの座標情報を、ROS2のトピック間通信により行います。

# 動作環境
- 確認環境
    - Ubuntu 20.04 LTS (WSL2)
    - Python 3.10
    - ROS2 foxy
- Github Actionsによるテスト
    - Ubuntu 22.04
    - Docker ryuichiueda/ubuntu22.04-ros2:latest

# 導入方法
ROS2の導入をしていない場合、[この資料の10ページ～](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)を参考にして、導入を行ってください。
<BR>
次に、リポジトリのクローンをします。
```bash
mkdir ~/ros2_ws/src
cd ~/ros2_ws/src
git clone git@github.com:s23c1130/mypkg.git
```
次に、```test_local.bash```の実行権限を付与し、実行します。
```bash
cd ~/ros2_ws/src/mypkg/test
chmod +x test_local.bash
./test_local.bash
```

```test_local.bash```を実行すると、このプログラムの動作に必要な```xdotool```,  ```pip``` , ```pyautogui```, ```python-xlib```が自動でインストールされます。<BR>
実行すると、パスワードを求められることがあります。パスワードを入力し、続行してください。

# ノード
マウスの座標を送信します。

## トピック
### x_pos
 - マウスのX軸座標
### y_pos
 - マウスのY軸座標

 # 謝辞
 プログラムを書く上で、参考にさせていただいたサイトです。ありがとうございました。<BR>
 - [Xvfb を利用したヘッドレスブラウザテスト](https://qiita.com/kt3k/items/cea3c6de3c2337004a84)
 - [pip3 install pyautogui, error code 1](https://stackoverflow.com/questions/48103873/pip3-install-pyautogui-error-code-1)

 # ライセンス
 - ```xdotool```はGPL-3.0 Licenseにて頒布されています。
   - https://www.gnu.org/licenses/gpl-3.0.ja.html
 - ```python-xlib```はGPL-2.1 Licenseにて頒布されています。
   - https://www.gnu.org/licenses/old-licenses/lgpl-2.1.ja.html
 - このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
 - このパッケージの一部のコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html