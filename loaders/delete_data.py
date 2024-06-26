# Custom imports
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
from utility.logging import setup_logging
from utility.database_handler import DatabaseHandler

# Initialise logging
logger = setup_logging()

##################################################################################################################################

def main():
    
    table_names = ["apple_blood_glucose", "apple_daily_activity", "apple_fitness_metrics", 
                   "apple_heart_rate", "apple_low_hr_events", "apple_running_metrics", 
                   "apple_sleep", "apple_steps", "apple_walking_metrics", "daylio_activities", 
                   "daylio_mood", "spend_transactions", "strava_performance_metrics", "strava_activity",
                   "youtube_likes_dislikes", "youtube_subscriptions"]

    # Initialise the DatabaseHandler
    db_handler = DatabaseHandler(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)    
    
    # Delete tables
    for table in table_names:
        db_handler.drop_table(table)
        
    # Close the database connection
    db_handler.close_connection()
   
if __name__ == "__main__":
    main()
