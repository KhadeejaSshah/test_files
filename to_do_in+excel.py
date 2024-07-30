# # import streamlit as st
# # import pandas as pd

# # # Load the Excel file
# # file_path = 'Skardu_Itinerary.xlsx'
# # df = pd.read_excel(file_path)

# # # Display the content of the Excel file
# # st.write("### Skardu Itinerary")
# # st.dataframe(df)

# # # Provide a download link for the Excel file
# # with open(file_path, 'rb') as f:
# #     st.download_button(
# #         label="Download Itinerary as Excel",
# #         data=f,
# #         file_name='Skardu_Itinerary.xlsx',
# #         mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
# #     )

# import pandas as pd
# import re
# import streamlit as st

# # Original itinerary text
# itinerary = """
# ### Overview of Skardu
# Skardu, located in the Gilgit-Baltistan region of Pakistan, is a beautiful town known for its stunning landscapes, crystal-clear lakes, and majestic mountains. This premium 3-day itinerary for Skardu includes visits to some of the most mesmerizing attractions, dining at top local restaurants, and comfortable accommodations.

# ### Day 1: 2024-07-29
# **Description**: Arrival and initial exploration of Skardu.

# **Details**:
# - **Morning**:
#   - **Activity**: Arrival and Check-in
#   - **Description**: Arrive at Skardu and check into your accommodation.
#   - **Accommodation**: abc (5-star rating, good view, amenities: wifi, pool, view)

# - **Midday**:
#   - **Activity**: Visit Shangrila Resort
#   - **Description**: Explore the beautiful Shangrila Resort, which includes activities like boating and jet skiing. Inclusive ticket price.

# - **Afternoon**:
#   - **Activity**: Lunch at hotel2
#   - **Description**: Enjoy a delicious lunch.
#   - **Cuisine**: Various

# - **Evening**:
#   - **Activity**: Visit Lower Kachura Lake
#   - **Description**: Enjoy the serene environment and activities available at Lower Kachura Lake. Inclusive ticket price.
#   - **Dining**: Dinner at hotel3

# ### Day 2: 2024-07-30
# **Description**: Exploring natural beauty and historical sites.

# **Details**:
# - **Morning**:
#   - **Activity**: Breakfast at hotel1
#   - **Description**: Enjoy a traditional Pakistani breakfast.

# - **Midday**:
#   - **Activity**: Visit Deosai National Park
#   - **Description**: Jeep ride through the beautiful Deosai National Park. Ticket price includes the jeep ride.

# - **Afternoon**:
#   - **Activity**: Lunch at hotel6
#   - **Description**: Enjoy your lunch before heading to more attractions.
#   - **Cuisine**: Various

# - **Evening**:
#   - **Activity**: Visit Sheosar Lake
#   - **Description**: Spend a serene evening at Sheosar Lake with activities inclusive in the ticket price.
#   - **Dining**: Dinner at hotel7

# ### Day 3: 2024-07-31
# **Description**: Final day of exploration and departure.

# **Details**:
# - **Morning**:
#   - **Activity**: Breakfast at hotel5
#   - **Description**: Have a hearty breakfast before your final day of exploration.

# - **Midday**:
#   - **Activity**: Visit Upper Kachura Lake
#   - **Description**: Enjoy activities at Upper Kachura Lake. Inclusive ticket price.

# - **Afternoon**:
#   - **Activity**: Lunch at hotel9
#   - **Description**: Savor your last lunch in Skardu.
#   - **Cuisine**: Various

# - **Evening**:
#   - **Activity**: Visit Katpana Desert (Cold Desert)
#   - **Description**: End your trip with a visit to the Cold Desert and enjoy the jeep ride. Inclusive ticket price.
#   - **Dining**: Dinner at hotel4
#   - **Activity**: Departure
#   - **Description**: Return to your accommodation to check out and prepare for departure.

# ### Excel Format Itinerary

# | Day          | Time         | Activity                     | Description                                           | Cost           |
# |--------------|--------------|------------------------------|-------------------------------------------------------|----------------|
# | 2024-07-29   | 9:00-10:00 am| Arrival and Check-in         | Arrive at Skardu and check into your accommodation    |                |
# |              | 11:00-12:00 pm| Visit Shangrila Resort       | Explore the resort, activities included                |                |
# |              | 1:00-2:00 pm | Lunch at hotel2              | Enjoy a delicious lunch                                |                |
# |              | 3:00-4:00 pm | Visit Lower Kachura Lake     | Serene environment, activities included                |                |
# |              | 7:00-8:00 pm | Dinner at hotel3             | Enjoy dinner at a local restaurant                     |                |
# | 2024-07-30   | 9:00-10:00 am| Breakfast at hotel1          | Traditional Pakistani breakfast                        |                |
# |              | 11:00-12:00 pm| Visit Deosai National Park   | Jeep ride through the park, activities included        |                |
# |              | 1:00-2:00 pm | Lunch at hotel6              | Savor your lunch before more exploration               |                |
# |              | 3:00-4:00 pm | Visit Sheosar Lake           | Enjoy the serene lake, activities included             |                |
# |              | 7:00-8:00 pm | Dinner at hotel7             | Enjoy dinner at a local restaurant                     |                |
# | 2024-07-31   | 9:00-10:00 am| Breakfast at hotel5          | Hearty breakfast before exploration                    |                |
# |              | 11:00-12:00 pm| Visit Upper Kachura Lake     | Enjoy the activities, ticket price included            |                |
# |              | 1:00-2:00 pm | Lunch at hotel9              | Savor your last lunch in Skardu                        |                |
# |              | 3:00-4:00 pm | Visit Katpana Desert         | Jeep ride through the Cold Desert, activities included |                |
# |              | 7:00-8:00 pm | Dinner at hotel4             | Enjoy dinner at a local restaurant                     |                |
# |              | 8:00-9:00 pm | Departure                    | Check out and prepare for departure                    |                |

# ### Total Cost Breakdown
# - **Accommodation**: 3 nights x 16,000 PKR/night = 48,000 PKR
# - **Dining**: 9 meals x 6,000 PKR/meal = 54,000 PKR
# - **Transportation**: 3 days x 15,375 PKR/day = 46,125 PKR
# - **Attractions**: 13,245 PKR
# - **Additional Costs**: 3 days x (500 PKR + 1,000 PKR + 1,500 PKR) = 9,000 PKR

# **Total Cost**: 48,000 + 54,000 + 46,125 + 13,245 + 9,000 = 170,370 PKR
# """

# # Split the itinerary into parts
# overview, *days = re.split(r"### Day \d+:", itinerary)

# # Process each day
# day_dict = {}
# for i, day in enumerate(days, start=1):
#     day_dict[f"day{i}"] = f"### Day {i}:{day.strip()}"

# # Extract Excel Format Itinerary
# excel_itinerary = re.findall(r'\| (.*?)\| (.*?)\| (.*?)\| (.*?)\| (.*?)\|', itinerary)

# # Create a DataFrame
# columns = ["Day", "Time", "Activity", "Description", "Cost"]
# df_itinerary = pd.DataFrame(excel_itinerary, columns=columns)

# # Save to an Excel file
# file_path = "tinerary.xlsx"
# df_itinerary.to_excel(file_path, index=False)

# st.write(day_dict.get("day1", "Day 1 not available"))
# st.write(day_dict.get("day2", "Day 2 not available"))


# # Display on Streamlit
# st.write("### Overview of Skardu")
# st.write(overview)

# # for key, value in day_dict.items():
# #     st.write(value)

# st.write("### Excel Format Itinerary")
# st.dataframe(df_itinerary)

# st.write("### Download Excel File")
# st.download_button(label="Download Itinerary", data=open(file_path, "rb").read(), file_name="tinerary.xlsx")


import pandas as pd
import re
import streamlit as st

# Original itinerary text
itinerary = """
### Overview of Skardu
Skardu, located in the Gilgit-Baltistan region of Pakistan, is a beautiful town known for its stunning landscapes, crystal-clear lakes, and majestic mountains. This premium 3-day itinerary for Skardu includes visits to some of the most mesmerizing attractions, dining at top local restaurants, and comfortable accommodations.

### Day 1: 2024-07-29
**Description**: Arrival and initial exploration of Skardu.

**Details**:
- **Morning**:
  - **Activity**: Arrival and Check-in
  - **Description**: Arrive at Skardu and check into your accommodation.
  - **Accommodation**: abc (5-star rating, good view, amenities: wifi, pool, view)

- **Midday**:
  - **Activity**: Visit Shangrila Resort
  - **Description**: Explore the beautiful Shangrila Resort, which includes activities like boating and jet skiing. Inclusive ticket price.

- **Afternoon**:
  - **Activity**: Lunch at hotel2
  - **Description**: Enjoy a delicious lunch.
  - **Cuisine**: Various

- **Evening**:
  - **Activity**: Visit Lower Kachura Lake
  - **Description**: Enjoy the serene environment and activities available at Lower Kachura Lake. Inclusive ticket price.
  - **Dining**: Dinner at hotel3

### Day 2: 2024-07-30
**Description**: Exploring natural beauty and historical sites.

**Details**:
- **Morning**:
  - **Activity**: Breakfast at hotel1
  - **Description**: Enjoy a traditional Pakistani breakfast.

- **Midday**:
  - **Activity**: Visit Deosai National Park
  - **Description**: Jeep ride through the beautiful Deosai National Park. Ticket price includes the jeep ride.

- **Afternoon**:
  - **Activity**: Lunch at hotel6
  - **Description**: Enjoy your lunch before heading to more attractions.
  - **Cuisine**: Various

- **Evening**:
  - **Activity**: Visit Sheosar Lake
  - **Description**: Spend a serene evening at Sheosar Lake with activities inclusive in the ticket price.
  - **Dining**: Dinner at hotel7

### Day 3: 2024-07-31
**Description**: Final day of exploration and departure.

**Details**:
- **Morning**:
  - **Activity**: Breakfast at hotel5
  - **Description**: Have a hearty breakfast before your final day of exploration.

- **Midday**:
  - **Activity**: Visit Upper Kachura Lake
  - **Description**: Enjoy activities at Upper Kachura Lake. Inclusive ticket price.

- **Afternoon**:
  - **Activity**: Lunch at hotel9
  - **Description**: Savor your last lunch in Skardu.
  - **Cuisine**: Various

- **Evening**:
  - **Activity**: Visit Katpana Desert (Cold Desert)
  - **Description**: End your trip with a visit to the Cold Desert and enjoy the jeep ride. Inclusive ticket price.
  - **Dining**: Dinner at hotel4
  - **Activity**: Departure
  - **Description**: Return to your accommodation to check out and prepare for departure.

### Excel Format Itinerary

| Day          | Time         | Activity                     | Description                                           | Cost           |
|--------------|--------------|------------------------------|-------------------------------------------------------|----------------|
| 2024-07-29   | 9:00-10:00 am| Arrival and Check-in         | Arrive at Skardu and check into your accommodation    |                |
|              | 11:00-12:00 pm| Visit Shangrila Resort       | Explore the resort, activities included                |                |
|              | 1:00-2:00 pm | Lunch at hotel2              | Enjoy a delicious lunch                                |                |
|              | 3:00-4:00 pm | Visit Lower Kachura Lake     | Serene environment, activities included                |                |
|              | 7:00-8:00 pm | Dinner at hotel3             | Enjoy dinner at a local restaurant                     |                |
| 2024-07-30   | 9:00-10:00 am| Breakfast at hotel1          | Traditional Pakistani breakfast                        |                |
|              | 11:00-12:00 pm| Visit Deosai National Park   | Jeep ride through the park, activities included        |                |
|              | 1:00-2:00 pm | Lunch at hotel6              | Savor your lunch before more exploration               |                |
|              | 3:00-4:00 pm | Visit Sheosar Lake           | Enjoy the serene lake, activities included             |                |
|              | 7:00-8:00 pm | Dinner at hotel7             | Enjoy dinner at a local restaurant                     |                |
| 2024-07-31   | 9:00-10:00 am| Breakfast at hotel5          | Hearty breakfast before exploration                    |                |
|              | 11:00-12:00 pm| Visit Upper Kachura Lake     | Enjoy the activities, ticket price included            |                |
|              | 1:00-2:00 pm | Lunch at hotel9              | Savor your last lunch in Skardu                        |                |
|              | 3:00-4:00 pm | Visit Katpana Desert         | Jeep ride through the Cold Desert, activities included |                |
|              | 7:00-8:00 pm | Dinner at hotel4             | Enjoy dinner at a local restaurant                     |                |
|              | 8:00-9:00 pm | Departure                    | Check out and prepare for departure                    |                |

### Total Cost Breakdown
- **Accommodation**: 3 nights x 16,000 PKR/night = 48,000 PKR
- **Dining**: 9 meals x 6,000 PKR/meal = 54,000 PKR
- **Transportation**: 3 days x 15,375 PKR/day = 46,125 PKR
- **Attractions**: 13,245 PKR
- **Additional Costs**: 3 days x (500 PKR + 1,000 PKR + 1,500 PKR) = 9,000 PKR

**Total Cost**: 48,000 + 54,000 + 46,125 + 13,245 + 9,000 = 170,370 PKR
"""
its = """
### Detailed Itinerary for Skardu (July 31, 2024 - August 3, 2024)

#### Overview:
Skardu, nestled in the Gilgit-Baltistan region of Pakistan, is a breathtaking destination known for its stunning landscapes, serene lakes, and majestic mountains. During this premium 4-day trip, you'll experience the natural beauty, rich culture, and adventure that Skardu has to offer.

#### Accommodations:
- **Hotel:** ABC
- **Location:** Good view
- **Amenities:** Wifi, pool, view
- **Rating:** 5 stars

---
### Day 1: July 31, 2024
#### Description: Arrival and exploration of local area

**Morning:**
- **Activity:** Arrival in Skardu and Check-in
- **Description:** Arrive at Skardu and check into the ABC Hotel. Freshen up and prepare for the day.

**Midday:**
- **Activity:** Visit Skardu Bazaar
- **Description:** Explore the vibrant Skardu Bazaar and shop for local handicrafts and souvenirs.

**Afternoon:**
- **Activity:** Lunch at Hotel2
- **Description:** Enjoy a delicious lunch at Hotel2 offering a variety of local and international cuisines.

**Evening:**
- **Activity:** Relax at the hotel pool
- **Description:** Spend a relaxing evening at the hotel's pool and enjoy the scenic views.

---
### Day 2: August 1, 2024
#### Description: Sightseeing day

**Morning:**
- **Activity:** Visit Kharpocho Fort
- **Description:** Start your day with a visit to Kharpocho Fort, offering panoramic views of Skardu.

**Midday:**
- **Activity:** Lunch at Hotel6
- **Description:** Savor a sumptuous lunch at Hotel6, known for its diverse menu and cozy ambiance.

**Afternoon:**
- **Activity:** Explore Lower Kachura Lake
- **Description:** Head to Lower Kachura Lake for a serene experience with activities like boating and jet skiing.

**Evening:**
- **Activity:** Dinner at Hotel4
- **Description:** Enjoy a delightful dinner at Hotel4, famous for its delicious meals and excellent service.

---
### Day 3: August 2, 2024
#### Description: Adventure and nature exploration

**Morning:**
- **Activity:** Visit Deosai National Park
- **Description:** Embark on a jeep ride to Deosai National Park and experience its vast plains and wildlife.

**Midday:**
- **Activity:** Picnic at Sheosar Lake
- **Description:** Enjoy a picnic lunch by the stunning Sheosar Lake, known for its crystal-clear waters.

**Afternoon:**
- **Activity:** Explore Katpana Desert (Cold Desert)
- **Description:** Visit the unique Cold Desert, Katpana Desert, and take a jeep ride to explore its sandy dunes.

**Evening:**
- **Activity:** Dinner at Hotel7
- **Description:** End your adventurous day with a delicious dinner at Hotel7.

---
### Day 4: August 3, 2024
#### Description: Cultural immersion and departure

**Morning:**
- **Activity:** Visit Shigar Fort
- **Description:** Start your day with a visit to Shigar Fort, a historic fort turned into a heritage hotel.

**Midday:**
- **Activity:** Lunch at Hotel9
- **Description:** Have a delectable lunch at Hotel9 before continuing your exploration.

**Afternoon:**
- **Activity:** Visit Satpara Lake
- **Description:** Explore the scenic Satpara Lake and indulge in activities like boating and jet skiing.

**Evening:**
- **Activity:** Departure
- **Description:** Return to the hotel, check out, and prepare for your departure from Skardu.

---

### Excel Format Itinerary:

| Day        | Time            | Activity                       | Description                                                                                  |
|------------|-----------------|--------------------------------|----------------------------------------------------------------------------------------------|
| July 31    | 9:00-10:00 am   | Arrival and Check-in           | Arrive at Skardu and check into the ABC Hotel                                                |
| July 31    | 10:00-12:00 pm  | Visit Skardu Bazaar            | Explore the vibrant Skardu Bazaar                                                            |
| July 31    | 12:00-1:00 pm   | Lunch at Hotel2                | Lunch at Hotel2                                                                              |
| July 31    | 1:00-3:00 pm    | Explore Skardu Bazaar          | Continue exploring Skardu Bazaar                                                             |
| July 31    | 3:00-5:00 pm    | Relax at the hotel pool        | Relax and enjoy the hotel amenities                                                           |
| July 31    | 5:00-7:00 pm    | Dinner at Hotel3               | Dinner at Hotel3                                                                             |
| August 1   | 9:00-10:00 am   | Visit Kharpocho Fort           | Visit Kharpocho Fort                                                                         |
| August 1   | 10:00-12:00 pm  | Explore Kharpocho Fort         | Continue exploring Kharpocho Fort                                                            |
| August 1   | 12:00-1:00 pm   | Lunch at Hotel6                | Lunch at Hotel6                                                                              |
| August 1   | 1:00-3:00 pm    | Explore Lower Kachura Lake     | Visit Lower Kachura Lake                                                                     |
| August 1   | 3:00-5:00 pm    | Activities at Lower Kachura Lake| Boating and jet skiing at Lower Kachura Lake                                                 |
| August 1   | 5:00-7:00 pm    | Dinner at Hotel4               | Dinner at Hotel4                                                                             |
| August 2   | 9:00-10:00 am   | Visit Deosai National Park     | Jeep ride to Deosai National Park                                                            |
| August 2   | 10:00-12:00 pm  | Explore Deosai National Park   | Explore the vast plains and wildlife of Deosai National Park                                 |
| August 2   | 12:00-1:00 pm   | Picnic at Sheosar Lake         | Picnic lunch at Sheosar Lake                                                                 |
| August 2   | 1:00-3:00 pm    | Explore Katpana Desert         | Jeep ride to Katpana Desert                                                                  |
| August 2   | 3:00-5:00 pm    | Activities in Katpana Desert   | Explore the sandy dunes of Katpana Desert                                                    |
| August 2   | 5:00-7:00 pm    | Dinner at Hotel7               | Dinner at Hotel7                                                                             |
| August 3   | 9:00-10:00 am   | Visit Shigar Fort              | Visit Shigar Fort                                                                            |
| August 3   | 10:00-12:00 pm  | Explore Shigar Fort            | Continue exploring Shigar Fort                                                               |
| August 3   | 12:00-1:00 pm   | Lunch at Hotel9                | Lunch at Hotel9                                                                              |
| August 3   | 1:00-3:00 pm    | Visit Satpara Lake             | Visit Satpara Lake                                                                           |
| August 3   | 3:00-5:00 pm    | Activities at Satpara Lake     | Boating and jet skiing at Satpara Lake                                                       |
| August 3   | 5:00-7:00 pm    | Departure                      | Return to the hotel, check out, and prepare for departure                                    |

Enjoy your premium trip to Skardu!
"""
hello = """
Generated Itinerary:

## Skardu Trip Itinerary (August 1, 2024 - August 4, 2024)

### Overview
Skardu, nestled in the Gilgit-Baltistan region of Pakistan, is a breathtaking destination surrounded by towering mountains, serene lakes, and historical forts. The town is a gateway to some of the world's highest peaks, including K2. The trip will include a mix of natural landscapes, historical sites, and cultural experiences.

### Accommodations
**Stay at "abc" in Skardu**  
Location: Good view  
Amenities: WiFi, Pool, Scenic View  
Rating: 3 Stars

### Day 1: August 1, 2024 - Arrival and Exploration
**Details:**
- **Morning:**
  - Arrival at Skardu and check-in at "abc"
- **Midday:**
  - Visit Shangrila Resort for a relaxing afternoon.  
    **Attraction Details:**  
    - Activities include boating and jet skiing.
- **Afternoon:**
  - Explore Lower Kachura Lake.  
    **Attraction Details:**  
    - Activities include boating and jet skiing.
- **Evening:**
  - Dinner at "hotel21"

### Day 2: August 2, 2024 - Natural Wonders
**Details:**
- **Morning:**
  - Visit Upper Kachura Lake  
    **Attraction Details:**  
    - Activities include boating and jet skiing.
- **Midday:**
  - Head to Satpara Lake  
    **Attraction Details:**  
    - Activities include boating and jet skiing.
- **Afternoon:**
  - Explore Deosai National Park via jeep  
    **Attraction Details:**  
    - Enjoy the scenic beauty and wildlife.
- **Evening:**
  - Dinner at "hotel21"

### Day 3: August 3, 2024 - Historical and Cultural Sites
**Details:**
- **Morning:**
  - Visit Shigar Fort  
    **Attraction Details:**  
    - Explore the historical fort and its museum.
- **Midday:**
  - Explore the Skardu Bazaar for local shopping and cultural experience.
- **Afternoon:**
  - Visit the Chaqchan Mosque  
    **Attraction Details:**  
    - A historical mosque known for its unique architecture.
- **Evening:**
  - Dinner at "hotel21"

### Day 4: August 4, 2024 - Adventure and Departure
**Details:**
- **Morning:**
  - Head to Manthokha Waterfall  
    **Attraction Details:**  
    - Activities include boating and jet skiing.
- **Midday:**
  - Visit Katpana Desert (Cold Desert) via jeep  
    **Attraction Details:**  
    - Enjoy the unique cold desert landscape.
- **Afternoon:**
  - Return to "abc" for check-out and departure.

---

## Skardu Trip Itinerary (Excel Format)

| Day         | Time           | Activity                            | Description                                                                                 |
|-------------|----------------|-------------------------------------|---------------------------------------------------------------------------------------------|
| August 1, 2024 | 9:00-10:00 AM  | Arrival                             | Arrival at Skardu and check-in at "abc"                                                     |
| August 1, 2024 | 11:00-1:00 PM  | Shangrila Resort                   | Visit Shangrila Resort; activities include boating and jet skiing                           |
| August 1, 2024 | 2:00-4:00 PM   | Lower Kachura Lake                 | Explore Lower Kachura Lake; activities include boating and jet skiing                       |
| August 1, 2024 | 7:00-9:00 PM   | Dinner                             | Dinner at "hotel21"                                                                         |
| August 2, 2024 | 9:00-11:00 AM  | Upper Kachura Lake                 | Visit Upper Kachura Lake; activities include boating and jet skiing                         |
| August 2, 2024 | 12:00-2:00 PM  | Satpara Lake                       | Head to Satpara Lake; activities include boating and jet skiing                             |
| August 2, 2024 | 3:00-5:00 PM   | Deosai National Park               | Explore Deosai National Park via jeep; enjoy the scenic beauty and wildlife                 |
| August 2, 2024 | 7:00-9:00 PM   | Dinner                             | Dinner at "hotel21"                                                                         |
| August 3, 2024 | 9:00-11:00 AM  | Shigar Fort                        | Visit Shigar Fort; explore the historical fort and its museum                               |
| August 3, 2024 | 12:00-2:00 PM  | Skardu Bazaar                      | Explore the Skardu Bazaar for local shopping and cultural experience                        |
| August 3, 2024 | 3:00-5:00 PM   | Chaqchan Mosque                    | Visit the Chaqchan Mosque; known for its unique architecture                                |
| August 3, 2024 | 7:00-9:00 PM   | Dinner                             | Dinner at "hotel21"                                                                         |
| August 4, 2024 | 9:00-11:00 AM  | Manthokha Waterfall                | Head to Manthokha Waterfall; activities include boating and jet skiing                      |
| August 4, 2024 | 12:00-2:00 PM  | Katpana Desert (Cold Desert)       | Visit Katpana Desert (Cold Desert) via jeep; enjoy the unique cold desert landscape         |

"""

helan = """

Overview
Destination Overview: Skardu, a town located in the Gilgit-Baltistan region of Pakistan, is a treasure trove of natural beauty and historical heritage. Nestled in the mighty Karakoram Range, Skardu is the gateway to some of the world's highest peaks, including the famed K2. This itinerary will take you through a mesmerizing journey of Skardu's lakes, valleys, ancient forts, and much more.
Day1
Day 1 (2024-07-30) Description: Arrival and Local Exploration 
Details:
Morning: Arrival at Skardu. Check-in at the ABC hotel, freshen up and enjoy a hearty breakfast at Hotel1. 
Midday: Visit the bustling Skardu Bazaar, a perfect place to observe local life and buy some souvenirs.
Afternoon: Visit Chaqchan Mosque, one of the oldest mosques in the region.
Evening: Dine at Hotel2 for a taste of local cuisine.
Day2
Day 2 (2024-07-31) Description: Lakes and Resorts
Details:
Morning: After breakfast at Hotel5, head to Satpara Lake. Enjoy activities like boating and jet skiing.
Midday: Proceed to the Shangrila Resort for lunch and explore the scenic beauty.
Afternoon: Visit Lower Kachura Lake and Upper Kachura Lake.
Evening: Dine at Hotel4 and return to the hotel.
Day3
Day 3 (2024-08-01) Description: Forts and Valleys
Details:
Morning: Breakfast at Hotel5. Visit the Shigar Fort and explore its rich history.
Midday: Head to Kharpocho Fort, another historical landmark.
Afternoon: Visit the Hussainabad Valley and enjoy its serene beauty.
Evening: Enjoy dinner at Hotel7 and return to the hotel.
Day4
Day 4 (2024-08-02) Description: Adventure Day
Details:
Morning: After breakfast at Hotel8, head to Deosai National Park. A jeep ride will take you through this high-altitude park.
Midday: Visit Sheosar Lake and enjoy the stunning views.
Afternoon: Head to Katpana Desert (Cold Desert) for a unique experience. Another jeep ride awaits here.
Evening: Dine at Hotel6 and return to the hotel.
Day5
Day 5 (2024-08-03) Description: Waterfall and Base Camp
Details:
Morning: Breakfast at Hotel1. Head to Manthokha Waterfall and soak in the tranquil ambiance.
Midday: Visit the K2 Base Camp.
Afternoon: Visit Rama Lake and enjoy the serene environment.
Evening: Enjoy dinner at Hotel3 and return to the hotel.
Day6
Day 6 (2024-08-04) Description: Departure
Details:
Morning: After breakfast at Hotel9, check out from the hotel.
Rest of the day: Departure from Skardu

As an AI, I am unable to create an Excel document physically. But here is how your Excel itinerary would look like:

| Day          | Time            | Activity                       | Description                                                                                  |
|--------------|-----------------|--------------------------------|----------------------------------------------------------------------------------------------|
| Month Date   | 9:00-10:00 am   | abc                            | Arrive at abc and check into the ABC Hotel 


| Day        | Time            | Activity                       | Description                                                                                  |
|------------|-----------------|--------------------------------|----------------------------------------------------------------------------------------------|
| July 31    | 9:00-10:00 am   | Arrival and Check-in           | Arrive at Skardu and check into the ABC Hotel                                                |
| July 31    | 10:00-12:00 pm  | Visit Skardu Bazaar            | Explore the vibrant Skardu Bazaar                                                            |
| July 31    | 12:00-1:00 pm   | Lunch at Hotel2                | Lunch at Hotel2                                                                              |
| July 31    | 1:00-3:00 pm    | Explore Skardu Bazaar          | Continue exploring Skardu Bazaar                                                             |
| July 31    | 3:00-5:00 pm    | Relax at the hotel pool        | Relax and enjoy the hotel amenities                                                           |
| July 31    | 5:00-7:00 pm    | Dinner at Hotel3               | Dinner at Hotel3  

...and so on for each day
"""
def excel(itinerary):

  excel_itinerary = re.findall(r'\| (.*?)\| (.*?)\| (.*?)\| (.*?)\|', itinerary)
  print(excel_itinerary)
  if excel_itinerary:
  # Create a DataFrame
    columns = ["Day", "Time", "Activity", "Description"]
    df_itinerary = pd.DataFrame(excel_itinerary, columns=columns)

    # Save to an Excel file
    file_path = "tinerary.xlsx"
    df_itinerary.to_excel(file_path, index=False)


    # for key, value in day_dict.items():
    #     st.write(value)

    st.write("### Excel Format Itinerary")
    st.dataframe(df_itinerary)

    st.write("### Download Excel File")
    st.download_button(label="Download Itinerary", data=open(file_path, "rb").read(), file_name="tinerary.xlsx")
  else:
    st.write('no itinerary made')  

itinerary  = f'"""{helan}"""'
excel(str(itinerary))  
     
