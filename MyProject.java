package myproject_modification;

import SystemServer.AccountAndPassword;
import SystemServer.Server;
import java.util.Scanner;

public class MyProject {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Server s = new Server();
        LottoMachine lottomachine;

        String account;
        String password;
        int keyin;
        int count = 0;

        System.out.println("==========請登入樂透系統!==========");
        while (count < 3) {
            System.out.print("請輸入帳號：");
            account = sc.next();
            System.out.print("請輸入密碼：");
            password = sc.next();

            if (count == 3) {
                System.out.println("帳號或密碼輸入次數過多");
                System.out.println("即將啟動保護程序!!");
                break;
            }
            
            
            if (s.check(new AccountAndPassword(account, password))) {
                System.out.println("======歡迎登入本系統!!======");
            } else {
                System.out.println("!!!!帳號或密碼錯誤!!!!");
                count++;
                continue;
            }
            

            do {
                System.out.print("請選擇樂透類別 1)大樂透 2)威力彩 3)今彩539 4)結束：");
                keyin = sc.nextInt();

                if (keyin == 4) {
                    System.out.println("====即將結束本系統，歡迎再次蒞臨!====");
                    break;
                }
                if (keyin < 0 || keyin > 4) {
                    System.out.println("輸入錯誤請再輸入一次!!");
                    continue;
                }

                switch (keyin) {
                    case 1:
                        lottomachine = new LottoMachine();
                        lottomachine.setLottoState(LottoEnum.BIGLOTTO);
                        break;
                    case 2:
                        lottomachine = new LottoMachine();
                        lottomachine.setLottoState(LottoEnum.POWERLOTTO);
                        break;
                    case 3:
                        lottomachine = new LottoMachine();
                        lottomachine.setLottoState(LottoEnum.TODAYLOTTO);
                        break;
                }
                //break;
            } while (true);
            break;
        }
    }

}
