# Regulations.gov Scraper

This tool scrapes Regulations.gov comment information including the submitter name, organization and any attachments by document id. 

This is a very barebones tool! We haven't even provided a CLI. To run, ensure you have the Python `requests` library installed. (It comes with Anaconda; if you're new to Python, we recommend installing Anaconda and letting it do the heavy lifting for you.)

You'll also need to apply for an API key as described [here](https://regulationsgov.github.io/developers/).

Once you have Python and the `requests` library installed, and have received an API key, make the following changes:

1) API Key:

   In the line that reads
   ```
   api_key = '' # insert your api key between quotes
   ```
   copy your API key and paste it between the signle quotation marks:
   ```
   api_key = '(THE API KEY THAT YOU COPIED)'
   ```

2) Docket ID: 

   In the line that reads
   ```
   docket_id = '' # insert the docket id between quotes (e.g. VA-2016-VHA-0011)
   ```
   paste the docket ID between the single quotation marks:
   ```
   docket_id = '(THE DOCKET ID THAT YOU COPIED)' 
   ```
   
   The docket ID appears on the page for the set of comments you've selected:
   [A screenshot of the docket ID](https://user-images.githubusercontent.com/4257267/53193703-a7c20400-35df-11e9-9089-35157cd065bb.png)
  
3) Total number of documents:

   In the line that reads
   ```
   total_docs = 217568  # total number of documents, as indicated by the page for the given docket id
   ```
   paste the number of documents in place of the current value:
   ```
   total_docs = 14835
   ```
    
   The number of documents also appears on the page above:
   [A screenshot of the number of documents](https://user-images.githubusercontent.com/4257267/53193710-abee2180-35df-11e9-8fe0-a0cd4e87d0f9.png)
