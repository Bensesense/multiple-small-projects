using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers; // Updated to correct namespace after installing the package


class Program
{
    static void Main()
    {
        // Set up the WebDriver (Chrome in this example)
        IWebDriver driver = new ChromeDriver();
        
        // Correctly initialize WebDriverWait
        WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));

        driver.Navigate().GoToUrl("https://www.eventim.de/event/weird-crimes-live-2024-olympiahalle-muenchen-17766476/?affiliate=TUG");

        try
        {
            // Attempt to wait for the cookie consent dialog to appear and find the "Deny All" button
            // Note: The actual XPath might need adjustment based on the specific website and its structure
            IWebElement denyButton = wait.Until(ExpectedConditions.ElementIsVisible(By.XPath("//button[contains(.,'erforder')]")));
            denyButton.Click();

            // Find the search box using its name attribute
            IWebElement searchBox = driver.FindElement(By.Name("q"));

            // Enter text to search for
            searchBox.SendKeys("OpenAI");

            // Submit the search
            searchBox.Submit();

            // Wait for a few seconds to see the results
            System.Threading.Thread.Sleep(5000); // This is not best practice for real projects
        }
        catch (NoSuchElementException ex)
        {
            Console.WriteLine($"Element not found: {ex.Message}");
        }
        catch (WebDriverTimeoutException ex)
        {
            Console.WriteLine($"Timeout waiting for element: {ex.Message}");
        }
        finally
        {
            // Close the browser and clean up
            driver.Quit();
        }
    }
}
