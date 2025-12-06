def load_dummy_data(player):
    
    taylor = player.library.add_artist("Taylor Swift")
    taylor.add_song(1, "Shake It Off", "3:39", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Pop")
    taylor.add_song(2, "Blank Space", "3:51", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Pop")
    taylor.add_song(3, "Style", "3:51", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Pop")
    taylor.add_song(4, "Love Story", "3:56", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Pop")
    taylor.add_song(5, "Anti-Hero", "3:21", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Pop")
    
    ed = player.library.add_artist("Ed Sheeran")
    ed.add_song(6, "Shape of You", "3:53", 
               "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Pop")
    ed.add_song(7, "Perfect", "4:23", 
               "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Pop")
    ed.add_song(8, "Castle on the Hill", "4:21", 
               "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Pop")
    ed.add_song(9, "Thinking Out Loud", "4:41", 
               "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Pop")
    ed.add_song(10, "Photograph", "4:18", 
               "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Pop")
    
    ariana = player.library.add_artist("Ariana Grande")
    ariana.add_song(11, "7 rings", "2:58", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Pop")
    ariana.add_song(12, "thank u, next", "3:27", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Pop")
    ariana.add_song(13, "positions", "2:52", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Pop")
    ariana.add_song(14, "Into You", "4:04", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Pop")
    
    dua = player.library.add_artist("Dua Lipa")
    dua.add_song(15, "Levitating", "3:23", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Pop")
    dua.add_song(16, "Don't Start Now", "3:03", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Pop")
    dua.add_song(17, "New Rules", "3:29", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Pop")
    
    coldplay = player.library.add_artist("Coldplay")
    coldplay.add_song(18, "Adventure of a Lifetime", "4:23", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Rock")
    coldplay.add_song(19, "Hymn for the Weekend", "4:18", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Rock")
    coldplay.add_song(20, "Viva La Vida", "4:01", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Rock")
    coldplay.add_song(21, "Fix You", "4:54", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Rock")
    coldplay.add_song(22, "Yellow", "4:26", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Rock")
    
    imagine = player.library.add_artist("Imagine Dragons")
    imagine.add_song(23, "Believer", "3:24", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Rock")
    imagine.add_song(24, "Thunder", "3:07", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Rock")
    imagine.add_song(25, "Whatever It Takes", "3:21", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Rock")
    imagine.add_song(26, "Radioactive", "3:06", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Rock")
    imagine.add_song(27, "Demons", "2:57", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Rock")
    
    onerepublic = player.library.add_artist("OneRepublic")
    onerepublic.add_song(28, "Counting Stars", "4:17", 
                        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Rock")
    onerepublic.add_song(29, "Apologize", "3:28", 
                        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Rock")
    onerepublic.add_song(30, "Good Life", "4:12", 
                        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Rock")
    
    maroon5 = player.library.add_artist("Maroon 5")
    maroon5.add_song(31, "Sugar", "3:55", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Rock")
    maroon5.add_song(32, "Girls Like You", "3:55", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Rock")
    maroon5.add_song(33, "Memories", "3:09", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Rock")
    
    weeknd = player.library.add_artist("The Weeknd")
    weeknd.add_song(34, "Starboy", "3:50", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "R&B")
    weeknd.add_song(35, "I Feel It Coming", "4:29", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "R&B")
    weeknd.add_song(36, "Blinding Lights", "3:22", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "R&B")
    weeknd.add_song(37, "Save Your Tears", "3:35", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "R&B")
    weeknd.add_song(38, "Die For You", "4:20", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "R&B")
    
    bruno = player.library.add_artist("Bruno Mars")
    bruno.add_song(39, "24K Magic", "3:46", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "R&B")
    bruno.add_song(40, "That's What I Like", "3:26", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "R&B")
    bruno.add_song(41, "Uptown Funk", "4:30", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "R&B")
    bruno.add_song(42, "Just The Way You Are", "3:40", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "R&B")
    
    sza = player.library.add_artist("SZA")
    sza.add_song(43, "Kill Bill", "2:33", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "R&B")
    sza.add_song(44, "Good Days", "4:39", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "R&B")
    sza.add_song(45, "I Hate U", "2:53", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "R&B")
    
    billie = player.library.add_artist("Billie Eilish")
    billie.add_song(46, "bad guy", "3:14", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Alternative")
    billie.add_song(47, "when the party's over", "3:16", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Alternative")
    billie.add_song(48, "Happier Than Ever", "4:58", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Alternative")
    billie.add_song(49, "ocean eyes", "3:20", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Alternative")
    
    tame = player.library.add_artist("Tame Impala")
    tame.add_song(50, "The Less I Know The Better", "3:36", 
                 "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Alternative")
    tame.add_song(51, "Let It Happen", "7:47", 
                 "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Alternative")
    tame.add_song(52, "Borderline", "3:58", 
                 "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Alternative")
    
    arctic = player.library.add_artist("Arctic Monkeys")
    arctic.add_song(53, "Do I Wanna Know?", "4:32", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Alternative")
    arctic.add_song(54, "505", "4:13", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Alternative")
    arctic.add_song(55, "Why'd You Only Call Me When You're High?", "2:41", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Alternative")
    
    marshmello = player.library.add_artist("Marshmello")
    marshmello.add_song(56, "Happier", "3:34", 
                       "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Electronic")
    marshmello.add_song(57, "Alone", "4:33", 
                       "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Electronic")
    marshmello.add_song(58, "Silence", "3:01", 
                       "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Electronic")
    
    chainsmokers = player.library.add_artist("The Chainsmokers")
    chainsmokers.add_song(59, "Closer", "4:04", 
                         "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Electronic")
    chainsmokers.add_song(60, "Don't Let Me Down", "3:28", 
                         "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Electronic")
    chainsmokers.add_song(61, "Something Just Like This", "4:07", 
                         "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Electronic")
    
    calvin = player.library.add_artist("Calvin Harris")
    calvin.add_song(62, "Summer", "3:43", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Electronic")
    calvin.add_song(63, "Feel So Close", "3:27", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Electronic")
    calvin.add_song(64, "This Is What You Came For", "3:44", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Electronic")
    
    drake = player.library.add_artist("Drake")
    drake.add_song(65, "God's Plan", "3:18", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Hip Hop")
    drake.add_song(66, "One Dance", "2:54", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Hip Hop")
    drake.add_song(67, "Hotline Bling", "4:27", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Hip Hop")
    
    post = player.library.add_artist("Post Malone")
    post.add_song(68, "Circles", "3:35", 
                 "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Hip Hop")
    post.add_song(69, "Sunflower", "2:38", 
                 "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Hip Hop")
    post.add_song(70, "Rockstar", "3:38", 
                 "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Hip Hop")
    
    travis = player.library.add_artist("Travis Scott")
    travis.add_song(71, "SICKO MODE", "5:12", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Hip Hop")
    travis.add_song(72, "goosebumps", "4:03", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Hip Hop")
    travis.add_song(73, "HIGHEST IN THE ROOM", "2:56", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Hip Hop")
    
    beatles = player.library.add_artist("The Beatles")
    beatles.add_song(74, "Come Together", "4:19", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Classic")
    beatles.add_song(75, "Here Comes the Sun", "3:05", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Classic")
    beatles.add_song(76, "Let It Be", "3:50", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Classic")
    beatles.add_song(77, "Hey Jude", "7:08", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Classic")
    
    queen = player.library.add_artist("Queen")
    queen.add_song(78, "Bohemian Rhapsody", "5:55", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Classic")
    queen.add_song(79, "We Will Rock You", "2:02", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Classic")
    queen.add_song(80, "Don't Stop Me Now", "3:29", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Classic")
    
    eagles = player.library.add_artist("Eagles")
    eagles.add_song(81, "Hotel California", "6:30", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Classic")
    eagles.add_song(82, "Take It Easy", "3:31", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Classic")
    eagles.add_song(83, "Desperado", "3:35", 
                   "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Classic")
    
    bts = player.library.add_artist("BTS")
    bts.add_song(84, "Dynamite", "3:19", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "K-Pop")
    bts.add_song(85, "Butter", "2:44", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "K-Pop")
    bts.add_song(86, "Boy With Luv", "3:49", 
                "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "K-Pop")
    
    blackpink = player.library.add_artist("BLACKPINK")
    blackpink.add_song(87, "DDU-DU DDU-DU", "3:29", 
                      "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "K-Pop")
    blackpink.add_song(88, "How You Like That", "3:02", 
                      "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "K-Pop")
    blackpink.add_song(89, "Pink Venom", "3:07", 
                      "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "K-Pop")
    
    newjeans = player.library.add_artist("NewJeans")
    newjeans.add_song(90, "Ditto", "3:05", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "K-Pop")
    newjeans.add_song(91, "OMG", "3:36", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "K-Pop")
    newjeans.add_song(92, "Super Shy", "2:34", 
                     "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "K-Pop")
    
    bad_bunny = player.library.add_artist("Bad Bunny")
    bad_bunny.add_song(93, "Tití Me Preguntó", "4:02", 
                      "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Latin")
    bad_bunny.add_song(94, "Callaita", "4:10", 
                      "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Latin")
    bad_bunny.add_song(95, "Dakiti", "3:25", 
                      "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3", "Latin")
    
    shakira = player.library.add_artist("Shakira")
    shakira.add_song(96, "Hips Don't Lie", "3:38", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3", "Latin")
    shakira.add_song(97, "Waka Waka", "3:22", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "Latin")
    shakira.add_song(98, "Whenever, Wherever", "3:16", 
                    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", "Latin")
    
    frank = player.library.add_artist("Frank Sinatra")
    frank.add_song(99, "Fly Me to the Moon", "2:29", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "Jazz")
    frank.add_song(100, "My Way", "4:35", 
                  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "Jazz")
