import sys
import time
from liveupstoxoc import live_upstox_oc
import upstox_login


n = live_upstox_oc.upstox_oc("/Users/sparshjhariya/Documents/chromedriver")

n.login(userid, password, twofa)