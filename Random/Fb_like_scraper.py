import pandas as pd

# Data for likes and non-likes
data = {
    "Name": [
        "Md Irfan", "Fäi Zäan", "Aindri Ghoshal", "Shubham Prasad Shaw", "Spenser Nawab", 
        "Sarfaraz Khan", "IamRohit Singhania", "Safwan Haider", "Shadab Hussain", "Zeeshan Ali",
        "Åhåń Verma", "Rj Gulshan", "Arun Kumar", "Dã Ñí SH", "Md Naushad Khan", "Mohit Shaw", 
        "Rohan Dey", "Fàî Sãll", "Aman Kumar Shaw", "Aditya Verma", "Ahana Mukherjee", "Amit Mandal", 
        "Arindam Ghosh", "Asima Biswas", "Avay Shaw", "Ayat Shamim", "Deepa Sarkar", "Disha Roy", 
        "Gourav Shaw", "Guddu Paa", "Husayn Ibn Ali", "Imran Aziz", "Imran Hasmi", "Jamir Ansari", 
        "Kavya Jaiswal", "Koushik Debnath", "Ma Zî D", "Manjit Singh", "Martal Art Guru", "Md Altaf", 
        "Md Imran", "Md Kaif Ansari", "Md Salman", "Md Shamsuddin", "Md Shakeel", "Md Tasneem", 
        "Monali Sanyal", "Muskan Mandal", "Nasim Ansari", "Nitish Shaw", "Poulami Dasgupta", 
        "Pritam Palit", "Pritesh Rajput", "Raman Shukla", "Ritesh Sarkar", "Rocky Acharjee", 
        "Rupashri Barik", "Samar Pratap Singh", "Shahid Khan", "Shahnawaz Khan", "Shaurya Kumar", 
        "Shubham Das", "Soumyadip Nath", "Sumit Dhar", "Warish Ansari"
    ],
    "Likes": [
        7, 6, 6, 7, 3, 3, 6, 3, 5, 5, 6, 6, 6, 6, 8, 7, 6, 6, 6, "No likes", "No likes", "No likes", 
        "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", 
        "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", 
        "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", 
        "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", 
        "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", "No likes", 
        "No likes", "No likes", "No likes", "No likes"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Replace "No likes" with 0 and convert the Likes column to numeric
df['Likes'] = df['Likes'].replace("No likes", 0).astype(int)

# Sort the DataFrame
df_sorted = df.sort_values(by=['Likes', 'Name'], ascending=[False, True])

# Save to CSV
file_path = "/fb_likes_list.csv"
df_sorted.to_csv(file_path, index=False)

file_path
