# XPath Homework – Task 1

## 1. Locate the main header element
**XPath:** `//h1[@id='mainTitle']`  
**Text on the page:** Welcome to Our Company

## 2. Select the "About Us" navigational link
**XPath:** `//nav//a[text()='About Us']`  
**Text:** About Us

## 3. Select the "Graphic Design" dropdown link
**XPath:** `//ul[@class='dropdown']//a[text()='Graphic Design']`  
**Text:** Graphic Design

## 4. Select the team member's name "Jane Smith"
**XPath:** `//div[@class='team']//h4[text()='Jane Smith']`  
**Text:** Jane Smith

## 5. Select the description of "SEO Services"
**XPath:** `//div[@class='service-item'][h3='SEO Services']/p`  
**Text:** Improving search engine rankings.

## 6. Select all service items in the "Our Services" section
**XPath:** `//section[@id='services']//div[@class='service-item']`  
**Text:** Web Development, Graphic Design, SEO Services

## 7. Select the email input field in the contact form
**XPath:** `//form[@id='contactForm']//input[@id='email']`  
**Attribute (id):** email

## 8. Select the entire contact form
**XPath:** `//form[@id='contactForm']`  
**Element:** form

## 9. Select the footer paragraph element
**XPath:** `//footer/p`  
**Text:** © 2023 Company Name. All rights reserved.

## 10. Select the first team member's name
**XPath:** `(//div[@class='team']//h4)[1]`  
**Text:** John Doe

## 11. Select the description of the second service item
**XPath:** `(//div[@class='service-item']/p)[2]`  
**Text:** Designing visual content.

## 12. Select the "Contact Us" section header
**XPath:** `//section[@id='contact']//h2[text()='Contact Us']`  
**Text:** Contact Us

## 13. Select all links within the dropdown under "Services"
**XPath:** `//li[a[text()='Services']]//ul[@class='dropdown']//a`  
**Text:** Web Development, Graphic Design, SEO Services

## 14. Select the first li under the "Our Team" section
**XPath:** `(//div[@class='team']//li)[1]`  
**Text:** John Doe

## 15. Locate the "Send Message" button in the contact form
**XPath:** `//form[@id='contactForm']//input[@type='submit' and @value='Send Message']`  
**Attribute (value):** Send Message
