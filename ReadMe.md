# serverless-slack-dad-jokes

serverless app that will post to slack with jokes from [wesbos/dad-jokes](https://github.com/wesbos/dad-jokes/) :v:

## Requirements

* Node and npm
* An aws account
* A slack channel

## Getting started

1. Install serverless
2. Configure your aws account with serverless
3. Deploy
4. Get yourself a webhook url [from here](https://my.slack.com/services/new/incoming-webhook/)
5. Set the webhook url in lambda's `SLACK_WEBHOOK_URL` env var
6. Invoke the function 

```bash
npm i -g serverless
sls deploy
sls invoke -f main --log
```
