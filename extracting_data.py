import requests
import pandas as pd

def request_data():
    url = "https://www.facebook.com/api/graphql/"

    payloads = 'av=100071338542737&__user=100071338542737&__a=1&__req=k&__hs=19557.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=MODERATE&__rev=1007859316&__s=u58aox%3Aidpr3j%3A0buweb&__hsi=7257470411375872213&__dyn=7AzHK4HzEmwIxt0mUyEqxenFwLBwopU98nwgUao4u5QdwSxucyUco5S3O2Saw8i2S1DwUx60DUG0Z82_CxS320om78bbwto88422y11xmfz81s8hwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E6a1TxWm2Sq2-azo7u3C223908O3216xi4UdUcojxK2B0oobo8oC1Hg6C&__csr=goiNcZ8gT5tAdlrlpcCIvlLaZ95FObbsALREzajEAGkB9dfZh1dEBQO69KjuZiddaXCdnOvuZAuAimSihuGyKAVVF94mtll3azuy6z4a-nCCByFGKq212r_CBiAyoWiAi9BhbAyUKUnUKmuupa5UkxemimUixyaQbz98G2OewFyoaFoSEyaxW3yQEG4EnCAzUjyohzEzgsUy3-m6ay8C8yqxm2C68lCxim7Ujxm18HzEaEtxeeBCAwHAw-woo6m1cxO79ogwFxSEbE4G1cwlE5G07IUc400Tk80cXU2Lwzw4Hg15U0jIw9C1Fx61Sg1moy5ESbw9J7wnU6S1Cw3pocE0KAw0Nt00PLw3882x810am9Dw2sQ0uqmlyrOuiy55eDw6hw1Nm07DQ1Tw2x20Hw2dE1xk0aJw35U&__comet_req=15&fb_dtsg=NAcO4P-6bltcVeM1t7aqCNZq9mUmM6uKKR6yEuIXuUCFHPOb-DBwd_A%3A17%3A1689677728&jazoest=25364&lsd=_hg2AvqwtkSn7yk_PHrzgi&__spin_r=1007859316&__spin_b=trunk&__spin_t=1689761507&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22AQHRFUkwE3kTuMiDiCuMR3skM-3tJD9st1bIcuokBRGjLOC0jLtDvVAdYr78lFjRyNbPQi9Yn70RqPDfXvx5sCirXA%22%2C%22groupID%22%3A%22353719791773684%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22353719791773684%22%7D&server_timestamps=true&doc_id=7396994073660826'

    headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'datr=qQvyYoBqA9pexNblIU4nXdy6; sb=rb2MY_qMnYyrhAbeWVpA2jb8; c_user=100071338542737; xs=17%3AvPU1a4iP2kKdLg%3A2%3A1689677728%3A-1%3A5920%3A%3AAcWAnjDppKvndhvEbiv76JvfVqDBg7PsF3xNMzqR3w; fr=0CGTqwJKPOz2He8e6.AWVqm-tMO9LJVN4yC3eazvXkLsM.Bkt7DU.kH.AAA.0.0.Bkt7DU.AWVXCEKBV04; wd=917x625; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1689761517112%2C%22v%22%3A1%7D; c_user=100071338542737; fr=0gflQCdlUb6LdtYpY.AWVOveBLwtoIb97AFVI5N9VSav4.Bkt7ha.kH.AAA.0.0.Bkt7ha.AWVksz1A1T0; xs=17%3AvPU1a4iP2kKdLg%3A2%3A1689677728%3A-1%3A5920%3A%3AAcUeIGlbmCMWUEbtfASBWzjhBz8plSKydPWE-eIuBlw',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/groups/353719791773684/members',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'viewport-width': '917',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
    'x-fb-lsd': '_hg2AvqwtkSn7yk_PHrzgi'
    }
    profile_urls = []

    response = requests.request("POST", url, headers=headers, data=payloads)
    return response.json()

def get_data():
    data = request_data()
    Name = []
    Profile_url = []
    Image_url = []
    Join_date = []
    Verification = []

    i = 0
    while i<10:
        url = data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('url')
        name = data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('name')
        image_url = data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('profile_picture').get('uri')
        join_date = data.get('data').get('node').get('new_members').get('edges')[i].get('join_status_text').get('text')
        verif = data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('is_verified')
        Name.append(name)
        Profile_url.append(url)
        Image_url.append(image_url)
        Join_date.append(join_date)
        Verification.append(verif)
        i += 1
    
    df = pd.DataFrame({
        'User_Name': Name,
        'Profile_Url': Profile_url,
        'Image': Image_url,
        'Join Status': Join_date,
        'Verification': Verification
    })

    return df
