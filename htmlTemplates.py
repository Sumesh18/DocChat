css = '''
<style>
.chat-message {
    font-size: 18px; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #6C5F5B
}
.chat-message.bot {
    background-color: #99B080
}
.chat-message .avatar {
  width: 15%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://hotpotmedia.s3.us-east-2.amazonaws.com/8-xyr7KEZbg33X8yY.png?nc=1">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://hotpotmedia.s3.us-east-2.amazonaws.com/8-y5nbm5ec9CbO6SJ.png?nc=1">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''