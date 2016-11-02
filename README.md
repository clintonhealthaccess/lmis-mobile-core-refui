# lmis-mobile-core-refui

[![Build Status](http://52.78.205.75:8080/job/ref-ui/badge/icon)](http://52.78.205.75:8080/job/ref-ui/)

# Use the Ref UI app

Use this app to discover what lmis mobile core enables you to do!

The easiest way to install the app is to download directly from: http://52.78.205.75:8081/app-release.apk

But if you want to keep up with the **latest** distribution and receive **updates**, you'll need to:

1. Install f-droid from: https://f-droid.org/
2. Add http://52.78.205.75:8081 as a repository
3. Refresh the f-droid app and get the latest Ref UI app

# Check out the code

```shell
git clone https://github.com/clintonhealthaccess/lmis-mobile-core-refui.git
```

Clone the code and read code snippets of how lmis mobile core can be leveraged.

# Set up your server

```

docker run -d -p 8080:8080 -v /path/of/your/property/files:/usr/local/tomcat/webapps/extra/properties cuipengfei/openlmis2

```

*"/path/of/your/property/files"* need to be replaced with an actual path that contains your specific property files.

Take this as template: https://github.com/clintonhealthaccess/openlmis-devops/tree/master/deployment/configuration/files/env/prod

Change configuration as you need, most importantly, fill in the DB credentials.

# Build your own mobile app

You can either start anew or fork this repo.

Refer to https://github.com/clintonhealthaccess/lmis-mobile-core/wiki/User-guide for how to use lmis mobile core APIs.

# Distribute your app

If you want to distribute your app similarly to how this app is distributed, please refer to https://github.com/clintonhealthaccess/lmis-mobile-core/wiki/Jenkins#ref-ui-publish-to-fdroid and **adjust the parameters** for your own needs.
