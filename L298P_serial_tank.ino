int E1 = 10;
int M1 = 12;
int E2 = 11;
int M2 = 13;
int data = 0;
#define BEATTIME 200 //音を出している時間(msec)
#define SPEAKER 4 //スピーカーの出力ピン番号

void setup(){
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  tone(SPEAKER,262,BEATTIME) ; // ド
  delay(BEATTIME) ;
  Serial.begin(9600);//シリアル通信開始、転送速度は9600ビット/秒
}

void loop(){
  if(Serial.available() > 0){  
    String str = Serial.readStringUntil(';');
  
    if(str.substring(0,1) == "F"){
      String arg1 = str.substring(1,4);
      String arg2 = str.substring(4,7);
      int L_duty = arg1.toInt();
      int R_duty = arg2.toInt();
      tank_forward(L_duty, R_duty);
    }

    if(str.substring(0,1) == "B"){
      String arg1 = str.substring(1,4);
      String arg2 = str.substring(4,7);
      int L_duty = arg1.toInt();
      int R_duty = arg2.toInt();
      tank_back(L_duty, R_duty);
    }

    if(str.substring(0,1) == "R"){
      String arg1 = str.substring(1,4);
      String arg2 = str.substring(4,7);
      int L_duty = arg1.toInt();
      int R_duty = arg2.toInt();
      tank_right(L_duty, R_duty);
    }

    if(str.substring(0,1) == "L"){
      String arg1 = str.substring(1,4);
      String arg2 = str.substring(4,7);
      int L_duty = arg1.toInt();
      int R_duty = arg2.toInt();
      tank_left(L_duty, R_duty);
    }
    
    if(str.substring(0,1) == "S"){
      tank_stop();
    }
  }
}


void tank_forward(int L_duty, int R_duty){
  digitalWrite(M1, HIGH);
  digitalWrite(M2, HIGH);
  analogWrite(E1, L_duty);
  analogWrite(E2, R_duty);
  Serial.println("FORWARD");
}

void tank_back(int L_duty, int R_duty){
  digitalWrite(M1, LOW);
  digitalWrite(M2, LOW);
  analogWrite(E1, L_duty);
  analogWrite(E2, R_duty);
  Serial.println("BACKWARD");
}

void tank_right(int L_duty, int R_duty){
  digitalWrite(M1, HIGH);
  digitalWrite(M2, LOW);
  analogWrite(E1, L_duty);
  analogWrite(E2, R_duty);
  Serial.println("RIGHT");
}

void tank_left(int L_duty, int R_duty){
  digitalWrite(M1, LOW);
  digitalWrite(M2, HIGH);
  analogWrite(E1, L_duty);
  analogWrite(E2, R_duty);
  Serial.println("LEFT");
}

void tank_stop(){
  digitalWrite(M1, LOW);
  digitalWrite(M2, LOW);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
  Serial.println("STOP");
}
