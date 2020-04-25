from django.shortcuts import render

def home(request):
	import json
	import requests


	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=BAA0F427-0CC2-4461-A124-61C54F116AD8")
		

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
			pass
			continue



		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50)Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100)Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150)Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300)Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301-500)Health alert: everyone may experience more serious health effects."
			category_color = "hazardous"



		return render(request, 'home.html', {
			'api': api,
			'category_description': category_description,
			'category_color': category_color
			})
		

	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=BAA0F427-0CC2-4461-A124-61C54F116AD8")
		

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."



		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50)Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100)Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150)Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300)Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301-500)Health alert: everyone may experience more serious health effects."
			category_color = "hazardous"


		return render(request, 'home.html', {
			'api': api,
			'category_description': category_description,
			'category_color': category_color
			})

		

def about(request):
	return render(request, 'about.html', {})
