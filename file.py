import cv2
import mediapipe as mp
import random

# This determine winner based on gestures
def determine_winner(player_gesture, computer_gesture):
    if player_gesture == computer_gesture:
        return "It's a tie!"
    elif (player_gesture == 'rock' and computer_gesture == 'scissors') or \
         (player_gesture == 'scissors' and computer_gesture == 'paper') or \
         (player_gesture == 'paper' and computer_gesture == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to recognize hand gestures
def recognize_gesture(hand_landmarks):
   
    gestures = ['rock', 'paper', 'scissors']
    return random.choice(gestures)

def main():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to get hand landmarks
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Logic for recognizing gestures
                player_gesture = recognize_gesture(hand_landmarks)

               # Randomly select a gesture
                computer_gesture = random.choice(['rock', 'paper', 'scissors'])

                #Displays the recognised player gesture  
                cv2.putText(frame, f"Player: {player_gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(frame, f"Computer: {computer_gesture}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                # Determine the winner and display the result
                result = determine_winner(player_gesture, computer_gesture)
                cv2.putText(frame, result, (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Hand Gestured Game", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
