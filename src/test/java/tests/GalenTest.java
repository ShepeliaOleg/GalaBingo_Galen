package tests;

import base.GalenTestBase;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;

import java.io.IOException;

/**
 * Created by olegs on 9/18/2015.
 */
public class GalenTest extends GalenTestBase{

    private WebDriver driver;
    public static final String BASE_URL = "http://allegro.pl/";
    public static final String SPEC_PATH = "/spec/home-page-mobile.spec";
    public static final String SPECS_SECTION = "Header";
    public static final String REPORT_PATH = "target/galen-html-reports";
    public static final String ERROR_MESSAGE = "Error on the header";

    @Test (dataProvider = "devices")
    public void homePageMobile(TestDevice device) throws IOException, InterruptedException {
        load("/");
        Thread.sleep(5000);
        checkLayout(SPEC_PATH, device.getTags());

    }

    @Test (dataProvider = "devices")
    public void homePageDesktop (TestDevice device) throws IOException, InterruptedException {
        Thread.sleep(5000);
        checkLayout("/spec/home-desktop", device.getTags());
    }

}
