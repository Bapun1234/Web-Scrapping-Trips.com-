import re
import urllib.request
URL = "https://www.trip.com/hotels/list?city=1&countryId=1&checkin=2020/11/17&checkout=2020/11/18&optionId=1&optionType=City&directSearch=0&display=Beijing&crn=1&adult=2&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1&display=Bangkok&crn=1&adult=1&children=0&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=0"
site = urllib.request.urlopen(URL)
test1 = site.read()
hotel = re.findall("\w[A-Za-z.] * +",str(test1),re.IGNORECASE)
print(test1)
