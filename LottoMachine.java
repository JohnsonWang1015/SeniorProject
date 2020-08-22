package myproject_modification;

import java.time.LocalDate;
import java.util.HashSet;
import java.util.Random;
import java.util.TreeSet;

public class LottoMachine implements LottoTool{
    private int lottoNumber;
    
    public void setLottoState(LottoEnum state){
        switch(state){
            case BIGLOTTO:
                lottoNumber = 49;
                chooseNumber();
                openNumber();
                judgment();
                createTime();
                break;
            case POWERLOTTO:
                lottoNumber = 38;
                chooseNumber();
                openNumber();
                judgment();
                createTime();
                break;
            case TODAYLOTTO:
                lottoNumber = 39;
                chooseNumber();
                openNumber();
                judgment();
                createTime();
                break;
        }
    } 
    //------------------------------------------
    HashSet<Integer> hashSet;
    TreeSet<Integer> treeSet;
    
    @Override
    public void chooseNumber(){
        hashSet = new HashSet<>();
        while(hashSet.size() < 6){
            int temp = new Random().nextInt(lottoNumber)+1;
            hashSet.add(temp);
            //System.out.printf("加入 %d 是否成功：%b%n", temp,hashSet.add(temp));
        }
        System.out.println("下注號碼：" + hashSet);
        System.out.println("--------------------------------");
    }
    
    @Override
    public void openNumber(){
       treeSet = new TreeSet<>();
       while(treeSet.size() < 6){
           treeSet.add(new Random().nextInt(lottoNumber)+1);
       }
       System.out.println("開獎號碼：" + treeSet);
       System.out.println("--------------------------------");
    }
    
    @Override
    public void judgment(){
        int count = 0;
        String msg = "";
        for(int i : hashSet){
            if(treeSet.contains(i)){
                count++;
                msg = msg + i + " ";
            }
        }
        System.out.printf("中獎號碼：%s，共 %d 個%n", msg, count);
    }
    
    @Override
    public void createTime(){
        LocalDate date = LocalDate.now();
        System.out.println("建立時間：" + date);
    }
}
