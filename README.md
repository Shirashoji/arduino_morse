# arduino_morse
arduinoでPCから送られてきた信号を自動でモールス信号に変換する。  
PCからはPythonを使って送信する。  

## 使い方
### Ardunio側
ArduinoのGNDと10番のピンにLEDを繋ぐ。  
`receiver/receiver.ino` をArduinoで実行する。  
### PC側
`pip install -r requirements.txt` で必要なPythonのモジュールをインストールする。  
`morse_transmitter.py` の4行目 `/dev/cu.usbmodem14101` を適当に修正する。  
#### 文章を直接入力する場合
`morse_ transmitter.py` をPythonで実行する。  
Pythonを実行したら`TEXT: `と出てくるので、アルファベットでモールス信号にしたい文章を入力する。  
LEDがモールス信号に変換され点灯する。
#### 外部ファイルを読み込む場合
`morse_transmitter.py ファイル名` をPythonで実行する。  
LEDがモールス信号に変換され点灯する。  
