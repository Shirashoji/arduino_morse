# arduino_morse
arduinoでPCから送られてきた信号を自動でモールス信号に変換する。  
PCからはPythonを使って送信する。  

## 使い方
`pip install -r requirements.txt` で必要なPythonのモジュールをインストールする。  
`morse_ transmitter.py` の4行目 `/dev/cu.usbmodem14101` を適当に修正する。  
ArduinoのGNDと10番のピンにLEDを繋ぐ。  
`receiver/receiver.ino` をArduinoで実行する。  
`morse_ transmitter.py` をPythonで実行する。  
Pythonを実行したら`TEXT: `と出てくるので、アルファベットでモールス信号にしたい文章を入力する。  
LEDがモールス信号に変換され点灯する。