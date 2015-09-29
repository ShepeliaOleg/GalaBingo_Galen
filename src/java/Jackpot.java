import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.util.List;

/**
 * Created by olegs on 9/25/2015.
 */
public class Jackpot {


    public void jackpotsList (WebDriver driver){

        List <WebElement> jackpots = driver.findElements(By.xpath("//*[contains(@class, 'jackpot-ticker-wrap')]/span"));

        for(WebElement element: jackpots){

            //System.out.println(element.getText().split("£")[1]);
            System.out.println(element.getText());
            System.out.println(123);
        }
    }


    public static void main(String[] args) {
        WebDriver driver = new FirefoxDriver();
        driver.get("http://www.galacasino.com/jackpots");

        Jackpot jackpot = new Jackpot();
        jackpot.jackpotsList(driver);
        System.out.println(555);
    }

}
