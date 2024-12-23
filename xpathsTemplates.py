
// Thes examples are based on the Rahul Shetty login page

If Id is present 
css -> tagname#id (or)  #id        # For example input#username for the username field

If class attribute is present
css -> tagname.class (or)  .class  # For class simply use input.username for the field. Sometimes this might yield more elements than needed, in that case use strictly tagname.class instead.

Write css based on any Attribute
css -> [attribute='value']         # For attribute it would be [name='username']

Write css with traversing from parent to child
css -> parenttagname >> childtagname

If needs to write the locator based on text
text''

# CSS examples

[routerlink*='cart']

[placeholder*='Country']

# Another set of examples for differnt types of xpaths

//span[contains(text(),"Cancel")]

//div[1]/div[@role='Check']//button/img

//*[@aria-label="Cancel"]

//button[@data-testid="Cancel"]

//*[text()="Cancel"]

//span[text()="Mobile Deposit"]

/text[@innertext='XXXX XXXX XXXX 3095']

//div[@data-testid="Select"]

//div/ul[@role=”listbox”]/li[@data-testid="DATE"]

//input[@data-testid="DATE"]

//div[@aria-label='Table Headers']

//*[id=”upload-front-image-label”]

//img[contains(@aria-label,'Uploaded Front Image')]

//span[text()=”{}”]/following::img[1]

//li[@class='credit']

//*[@id=”menu-creditOrDebit”]/div[3]/ul/li[2]

//button[@id=”medium-dialog-submit”]

[href*="documents-request"]

//div[contains(@class, 'user__name')] or in the case of the dom that has both classes like this user__name mt-5 then this is also good //div[contains(@class, 'mt-5')]

//div[contains(@class, 'user__name')]/label[@type='text']  // type=text was added as a child to its parent 'user__name'

//div[contains(@id, 'courses-iframe')]

//*[@class='card-body']

//div[@class='card-body']//b      // This further targets and drills down to the label b from card-body


************************************************************************

Practice sites:

https://rahulshettyacademy.com/loginpagePractise/

https://rahulshettyacademy.com/client

https://rahulshettyacademy.com/AutomationPractice/

//*[@id="mz-filter-panel-0-3"]/div/input