from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup as bs
import re
import requests


# Function to remove HTML tags from a string
def remove_tags(text):
    return re.sub(r'<[^>]*>', '', text)

# Function to get Codeforces user rating
def codeforcesRating(username):
    try:
        profile = f'https://codeforces.com/profile/{username}'
        req = requests.get(profile)
        if req.status_code != 200:
            print("Failed to retrieve Codeforces profile page")
            return None

        soup = bs(req.text, 'html.parser')
        user_info = soup.find_all('span', class_='user-gray')
        if not user_info:
            print("No user information found")
            return None

        profile_data = {
            "Profile Link": profile,
            "Username": username,
            "Present Title": remove_tags(str(user_info[0])),
            "Maximum Title": remove_tags(str(user_info[-2])),
            "Present Rating": remove_tags(str(user_info[1])),
            "Maximum Rating": remove_tags(str(user_info[-1]))
        }

        return profile_data

        # print("\n+------------------+")
        # print("| Codeforces Profile |")
        # print("+--------------------+")
        # for key, value in profile_data.items():
        #     print(f"{key}: {value}")

    except Exception as e:
        print(f"Error fetching Codeforces profile: {e}")

# Function to get CodeChef user rating
def codechefRating(username):
    try:
        url = f"https://www.codechef.com/users/{username}"
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to retrieve CodeChef profile page")
            return None

        soup = bs(response.content, 'html.parser')
        profile_data = {
            "Profile Link": url,
            "Username": username,
            "Name": soup.find("h1", {"class": "h2-style"}).get_text(strip=True) if soup.find("h1", {"class": "h2-style"}) else "N/A",
            "Rating": soup.find("div", {"class": "rating-number"}).get_text(strip=True) if soup.find("div", {"class": "rating-number"}) else "N/A",
            "Stars": soup.find("span", {"class": "rating"}).get_text(strip=True) if soup.find("span", {"class": "rating"}) else "N/A",
            "Country": soup.find("span", {"class": "user-country-name"}).get_text(strip=True) if soup.find("span", {"class": "user-country-name"}) else "N/A",
            "Global Rank": soup.find("div", {"class": "rating-ranks"}).find("a").get_text(strip=True) if soup.find("div", {"class": "rating-ranks"}) else "N/A"
        }

        return profile_data

        # print("\n+------------------+")
        # print("| CodeChef Profile |")
        # print("+------------------+")
        # for key, value in profile_data.items():
        #     print(f"{key}: {value}")

    except Exception as e:
        print(f"Error fetching CodeChef profile: {e}")


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/codechef')
def codechef():
	return render_template('codechef.html')

@app.route('/submit',methods=['POST'])
def submittdData():
	codechefUsername = request.form['codechefUsername']
	codeforcesUsername = request.form['codeforcesUsername']

	print("Codechef Username:",codechefUsername)
	print("Codeforces Username:", codeforcesUsername)

	codechefProfile=codechefRating(codechefUsername)
	codeforcesProfile=codeforcesRating(codeforcesUsername)
	return render_template('index.html',codechef_profile_data=codechefProfile,codeforces_profile_data=codeforcesProfile)

@app.route('/codeforcesprofile',methods = ['POST'])
def codeforceProfile():
     username = request.form['codeforcesUsername']
     codeforcesProfile = codeforcesRating(username)
     print(codeforcesProfile)
     return render_template('codeforces.html',profile_data = codeforcesProfile)

@app.route('/codechefprofile',methods=['POST'])
def codechefProfile():
     username = request.form['codechefUsername']
     codechefProfile = codechefRating(username)
    #  print(codechefProfile)
     return render_template('codechef.html',profile_data = codechefProfile)

@app.route('/codeforces')
def codeforces():
	return render_template('codeforces.html')

if __name__ == "__main__":
	app.run(debug = True,port = 1234)