from torsel import Torsel

# Selenium function to invoke in the Torsel object
def collect_ip(driver, wait, EC, By):
    print("fetching")
    driver.get("http://ec2-98-80-254-138.compute-1.amazonaws.com")
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "some"))
    ip_address = driver.find_element(By.TAG_NAME, "h1").text.strip()
    print(ip_address)

# Torsel object
torsel = Torsel(headless=False, # Invoke Torsel in headless mode and run
                tor_path="/usr/sbin/tor", # path to executable
                tor_data_dir="/tmp/tor_profiles",
                verbose=True) # tor profiles path dest
torsel.run(1, collect_ip)
