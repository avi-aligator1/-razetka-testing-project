import requests
import json

url = "https://uss.rozetka.com.ua/session/cart-se/add"

payload = json.dumps([
  {
    " goods_id ": 400966992,
    "quantity": 1
  }
])
headers = {
  'contect-type': 'application/json',
  'Csrf-Token': 'f2yfDeepyKiXRANEH6SUepKLvHaUKlZKFmwhkfFURewgffeg',
  'Cookie': 'cart-modal=old; ab-auto-portal=old; promo-horizontal-filters=verticalFilters; social-auth=old; ab_tile_filter=old; xab_segment=31; uid=Cgo9D2XR7kAMqDY7gFOhAg==; _gcl_au=1.1.398095150.1708256831; __utmz_gtm=utmcsr=bing|utmccn=(none)|utmcmd=organic; _uss-csrf=f2yfDeepyKiXRANEH6SUepKLvHaUKlZKFmwhkfFURewgffeg; ussat_exp=1708300033; ussajwt=eyJhbGciOiJSUzI1NiIsImtpZCI6InVzc2F0LnYwIiwidHlwIjoiSldUIn0.eyJkZXRhaWxzIjoiNGYyNWVhODg3YzlkNDZiZDMzYzMzYjAwZGRlMmFkNThiYTZjODMzZDNjOTFiNTVkMWRlMjc3ZmU3MzE2NzU2ZTQwMDdlOWRiODU1ZWE3MjRhZjc3NmEwOWUwMjMyYjQxYmY5Zjc4NjUzMDM3ZjdiYzIzNDE2Y2E3OWNhNzdiMTA3YzQwMjVhY2UzOTkwNmNlY2NjYTc3YzkxY2U5MzA3ODdlZTgzYjVlZGRlOGI2ODIxYjk3M2RhNjQ4YjVjMjgwODM1MTRlZTRkNDkwYzhiMWRlYzgwYWI0NzMxYTRhMTA3N2RiOTE1M2M1NTdiMDZhNmQwOTg1N2ZhZTk5YmI5MyIsImV4cCI6IjE3MDgzMDAwMzMiLCJ1c3NhdCI6ImI2YTYzNzc1ZmMxOWYzMWFhMzMzYjNhODUzZTBkYmM4LnVhLTNhNzM5NDFmZWVmMWM0YzdkNDVkNjAwYzYzYjRkODY3LjE3MDgzMDAwMzMifQ.cGO9xa9IQs0LW_wMRo45t6u9dMXMcE2cLERe1quu53yH4RNiApn3ErEPjbx16Hs9jNjxXZpcGHCxGOBW_B8EwH7zGfbom4QbisE9VyZ_CHyK0RmZTFuy6MyR5rifgaVoexQyxxIj1oPAlVNmFGtU0L-BeB6FVjaxntBrnsARAqQ4f2EH1I4OHtU9A8EjcHD5s0_3DcyIuzV_bJZEJtxBwy1V52W05SwEl7LN8TEKURkKHHWtFxM_2Uma69UvUbFdL7bNDo5aiK3Ub17FRjNfW9_weXymBOm_ru1R99Jhupn4fnHfPm-8reN5Qz_JgZ6K1haWRK3p-sMFzvnUH5CFOw; ussat=b6a63775fc19f31aa333b3a853e0dbc8.ua-3a73941feef1c4c7d45d600c63b4d867.1708300033; ussrt=575244a56f31e59fea93ee95a59a015e.ua-3a73941feef1c4c7d45d600c63b4d867.1710848833; ussapp=X9L5Y2ZD8Qai9D6Ibt-Ri_bG5DSLcedUOtEt_lGw; _ga=GA1.3.234917349.1708256831; _hjSession_3494164=eyJpZCI6ImQ1MzQ3NTc2LTVkMjgtNDUxNi1hZmRjLTg4ZjU4NTY0OTE0MyIsImMiOjE3MDgyNTY4MzEzMjksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; city_id=b205dde2-2e2e-4eb9-aef2-a67c82bbdf27; _gid=GA1.3.1607157157.1708256831; afclid=27421910431708256834; __exponea_etc__=0b3eb57b-4715-48e0-892d-e55029a59311; __exponea_time2__=2.4536430835723877; _fbp=fb.2.1708256832719.1818164378; _hjSessionUser_3494164=eyJpZCI6ImM1ODhkNTAzLThhM2UtNTdlZC1hMmNlLTQ4OWRkNWRkYTA4ZCIsImNyZWF0ZWQiOjE3MDgyNTY4MzEzMjgsImV4aXN0aW5nIjp0cnVlfQ==; slang=ru; __gads=ID=7c32ba5a7a83247f:T=1708257020:RT=1708257020:S=ALNI_MYADkVZgZeioZOOweDwxltRnolm-Q; __gpi=UID=00000d264947f644:T=1708257020:RT=1708257020:S=ALNI_Mb1JncmNJQpjEeTb55KO-k-DuLlQA; __eoi=ID=86e503a4b0e2fe9d:T=1708257020:RT=1708257020:S=AA-AfjamfYdbLsO8rY3rp32BW8BO; __cf_bm=TXVhXQ6Apl5sTHdSFWCf6PpusH3zjfuZRfYe2AGjNrQ-1708257586-1.0-AQO+6JQR1OY/8qdSBc+FNUc4S6PylucnApd2iAgaa2ZsZ9Kzh4OkabxxHgCVFID+sscKzXJjKSNMtq9Xkb1hrO4=; cf_clearance=2m5Tk00uzDxp23Pc9doHLzTaP6RUUbcNg6aMRKUzrBI-1708257633-1.0-AbpSCd/WZRx24HvDLpTkk3z8CFnL4RZlchhksBilxv67oZYwmG+MARHxJhZ3S0eLBQQFeykVHXWmyeF0J5KlvNI=; _ga_3X15VBC9L9=GS1.3.1708256831.1.1.1708257631.0.0.0; cto_bundle=BjB8q196WHFIdmJad2dNblgzVmJybk9RdW9WZ0xqVHVlUUJFT0pJUDRsc09SRTFEaU9IOTRzZHFTa1BVWE9WUUlydTgwbHVocHkwMSUyQjRXUGRYRUVXaGo1M0lYRmhNVGdZJTJGalRuaHBCOHolMkZhU2FuUklkYmV0JTJGY2FsY0M4Y2NiNjNmSkVjZ2RHbjUzQmNRQiUyRlJFNUdSd1NTNlV3JTNEJTNE; _dc_gtm_UA-203518-6=1; __cf_bm=PghxpdJeZy7Se6O2nEAhWuhr25vDT5SP89i_9_DAoaI-1708258504-1.0-Af9yDRkx/fJjdQjS6+UGluRcyJ0nThEeymGedpNm8fuQ4uiSj8GCdr3icPAQclGJCq5uDNuwPWAPmyZyaMgrCuc=; _uss-csrf=fBwODM2ySGk+jFVe5hptXoL/lUrtt1bHMQv1SzhVRpJQiZq+; ussajwt=eyJhbGciOiJSUzI1NiIsImtpZCI6InVzc2F0LnYwIiwidHlwIjoiSldUIn0.eyJkZXRhaWxzIjoiNGYyNWVhODg3YzlkNDZiZDMzYzMzYjAwZGRlMmFkNThiYTZjODMzZDNjOTFiNTVkMWRlMjc3ZmU3MzE2NzU2ZTQwMDdlOWRiODU1ZWE3MjRhZjc3NmEwOWUwMjMyYjQxYmY5Zjc4NjUzMDM3ZjdiYzIzNDE2Y2E3OWNhNzdiMTA3YzQwMjVhY2UzOTkwNmNlY2NjYTc3YzkxY2U5MzA3ODdlZTgzYjVlZGRlOGI2ODIxYjk3M2RhNjQ4YjVjMjgwODM1MTRlZTRkNDkwYzhiMWRlYzgwYWI0NzMxYTRhMTA3N2RiOTE1M2M1NTdiMDZhNmQwOTg1N2ZhZTk5YmI5MyIsImV4cCI6IjE3MDgzMDAwMzMiLCJ1c3NhdCI6ImI2YTYzNzc1ZmMxOWYzMWFhMzMzYjNhODUzZTBkYmM4LnVhLTNhNzM5NDFmZWVmMWM0YzdkNDVkNjAwYzYzYjRkODY3LjE3MDgzMDAwMzMifQ.cGO9xa9IQs0LW_wMRo45t6u9dMXMcE2cLERe1quu53yH4RNiApn3ErEPjbx16Hs9jNjxXZpcGHCxGOBW_B8EwH7zGfbom4QbisE9VyZ_CHyK0RmZTFuy6MyR5rifgaVoexQyxxIj1oPAlVNmFGtU0L-BeB6FVjaxntBrnsARAqQ4f2EH1I4OHtU9A8EjcHD5s0_3DcyIuzV_bJZEJtxBwy1V52W05SwEl7LN8TEKURkKHHWtFxM_2Uma69UvUbFdL7bNDo5aiK3Ub17FRjNfW9_weXymBOm_ru1R99Jhupn4fnHfPm-8reN5Qz_JgZ6K1haWRK3p-sMFzvnUH5CFOw; ussapp=X9L5Y2ZD8Qai9D6Ibt-Ri_bG5DSLcedUOtEt_lGw; ussat=b6a63775fc19f31aa333b3a853e0dbc8.ua-3a73941feef1c4c7d45d600c63b4d867.1708300033; ussat_exp=1708300033; ussrt=575244a56f31e59fea93ee95a59a015e.ua-3a73941feef1c4c7d45d600c63b4d867.1710848833',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
