package SystemServer;

public class Server {
    public boolean check(AccountAndPassword ap){
        if(ap.getAccount().equals("abc") && ap.getPassword().equals("123")){
            return true;
        }
        return false;
    }
}
