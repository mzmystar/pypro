package mixTest;

import java.util.Scanner;

public class Login3Test {
    public static void main(String[] args){
        String admin = "superadmin";
        String passwd = "ad123";
        for(int i=1;i < 4;i++){
            Scanner sc = new Scanner(System.in);
            System.out.println("输入账号");
            String admin_test = sc.nextLine();
            System.out.println("输入密码");
            String passwd_test = sc.nextLine();
            if(admin.equals(admin_test) && passwd.equals(passwd_test)){
                System.out.println("successful");
                break;
            }else{
                System.out.println("failed,chance has "+(3-i));
            }
        }
    }
}
