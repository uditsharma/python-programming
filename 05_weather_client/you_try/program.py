import collections

import bs4
import requests

WeatherReport = collections.namedtuple("WeatherReport", "cond,temp,loc,scale")


def print_header():
    print("-------------------------")
    print("      WEATHER APP")
    print("-------------------------")


def get_html_from_web_for_zip(zip_code):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)
    return response.text


def clean_text(text: str):
    if not text:
        return text
    text = text.strip()
    return text


def get_city_and_state_from_location(location: str):
    parts = location.split("\n")
    return parts[0].strip()


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    location = clean_text(location)
    condition = clean_text(condition)
    temp = clean_text(temp)
    scale = clean_text(scale)

    return WeatherReport(cond=condition, temp=temp, loc=location, scale=scale)


def main():
    print_header()
    zip_code = input("Enter zip code for which you want to know the weather [500049]")
    zip_code = zip_code.strip()
    html = get_html_from_web_for_zip(zip_code)
    report = get_weather_from_html(html)
    print("Temp in {} is {} {} and {}".format(report.loc, report.temp, report.scale, report.cond))


if __name__ == '__main__':
    main()
