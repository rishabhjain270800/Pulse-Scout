import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Duplicate marquee items for seamless loop
marquee_items_1 = '''
                        <div class="pill"><span class="dot" style="background:#4285F4"></span> Google Search</div>
                        <div class="pill"><span class="dot" style="background:#EA4335"></span> Google Display</div>
                        <div class="pill"><span class="dot" style="background:#00A4EF"></span> Microsoft Bing</div>
                        <div class="pill"><span class="dot" style="background:#1877F2"></span> Meta</div>
                        <div class="pill"><span class="dot" style="background:#FF0000"></span> YouTube</div>
                        <div class="pill"><span class="dot" style="background:#E4405F"></span> Instagram</div>
'''
html = html.replace(marquee_items_1 + '                        <!-- Repeat -->', marquee_items_1 + marquee_items_1)

marquee_items_2 = '''
                        <div class="pill"><span class="dot" style="background:#1D6F42"></span> Excel</div>
                        <div class="pill"><span class="dot" style="background:#F40F02"></span> PDF Reports</div>
                        <div class="pill"><span class="dot" style="background:#F7941D"></span> PayU</div>
                        <div class="pill"><span class="dot" style="background:#4A154B"></span> Slack Alerts</div>
                        <div class="pill"><span class="dot" style="background:#D44638"></span> Email</div>
                        <div class="pill"><span class="dot" style="background:#3b82f6"></span> REST API</div>
'''
html = html.replace(marquee_items_2, marquee_items_2 + marquee_items_2)

# Duplicate feed items for seamless loop
feed_items = '''
                            <div class="mention-card">
                                <span class="badge pos">Positive</span>
                                <strong>Maruti Suzuki</strong>
                                <p>"The new Maruti Brezza feels incredibly solid and the fuel efficiency is just unbeatable in this segment."</p>
                                <div class="card-meta"><span>team-bhp.com</span> <span>2 hours ago</span></div>
                            </div>
                            <div class="mention-card">
                                <span class="badge neg">Negative</span>
                                <strong>Zomato</strong>
                                <p>"Extremely disappointed with the delivery time today. 90 minutes for a 2km distance? Unacceptable."</p>
                                <div class="card-meta"><span>twitter.com</span> <span>1 hour ago</span></div>
                            </div>
                            <div class="mention-card">
                                <span class="badge neu">Neutral</span>
                                <strong>HDFC Bank</strong>
                                <p>"Comparing HDFC and ICICI home loan rates for my new apartment. Both seem competitive this quarter."</p>
                                <div class="card-meta"><span>moneycontrol.com</span> <span>3 hours ago</span></div>
                            </div>
                            <div class="mention-card">
                                <span class="badge pos">Positive</span>
                                <strong>Flipkart</strong>
                                <p>"Amazing experience with Flipkart Minutes! Got my groceries in less than 15 minutes. Game changer."</p>
                                <div class="card-meta"><span>facebook.com</span> <span>30 mins ago</span></div>
                            </div>
'''
html = html.replace(feed_items + '                            <!-- Repeat for smooth scroll -->', feed_items + feed_items)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
