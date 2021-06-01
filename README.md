# Chadni Project
- [Component List](#list-of-components)
- [Design](#design)
- [Building Process](#building-process)
- [Results](#results)
## List of Components
* Aluminium Sheets --- 2 x $16
* Dayton DAEX25FHE-4 Audio Exciter --- 2 x $13.87
* DAMGOO Bluetooth Audio Amplifier --- 1 x $18.99
* Power Supply --- Sam check this
* Carriage Bolts --- 4 x $0.84
* Brass 6x1-1/2 Machine Screws --- 6 x $1.20
* 1/4 Inch Zinc Wingnut --- 4 x $1.18
* Tin Snips --- 1 x 13.98
* PVC 4" to 2" Reducer --- 1 x $8.97
* PVC 2" Bushing --- 1 x $2.07
* PVC 3/4" Endcaps --- 4 x $0.75
* 20 Pack Right Angle Brackets --- $7.98
* Loctite Epoxy --- 1 x $6.51
* Black and Red 14 AWG Gauge Wire --- $12.98
* Essential Everyday Iodized Salt --- 2 x $1.98
* BLASTER 9.30 oz Dry Lub w/ PTFW --- 1 x $4.48
* 20" Hand Saw --- 1 x $13.97
* 10-12" Hacksaw and Blade --- 1 x $9.51
* Rustoleum Protective Enamel --- 1 x $4.58
* Black Vinyl Electric Tape 10 pack --- $7.98
* Pen Shaft --- Free, courtesy of Gabrielle Carrel
* Drill/Drill Bit/Battery --- Free, courtesy of Sam Alcott
* Random bits of Plywood --- Free, courtesy of past/present members of the Faux Op

## Design
Our design is centered around the use of an audio exciter, a device conventionally used to generate sound by mechanically vibrating ordinary surfaces as part of exotic sound systems. More information about them, particularly the brand we used, can be found [here](https://www.daytonaudio.com/category/180/exciters).

Unfortunately, the task at hand was to drive a plate up and down, not conceal a surround sound system. We do this by (surprise surprise) attaching the plate to the audio exciter, albeit our setup is a little more complicated than that. The exciter is mounted to a piece of crap plywood, and the plate is connected to the exciter via a carriage bolt which raises it a good height above the platform. This allows the bolt to be run through a stabilization chamber that keeps the plate more or less level. The fine details of this entire construction will be discussed in the next section.

A good deal of our design was inspired by the one found [here](https://www.instructables.com/Oobleck-Chladni-Plate/).

## Building Process

Possibly the biggest obstacle in out building process was getting the darn plate level so the salt wouldn't pile off as soon as we turned the exciter on. This was a more complicated problem than we anticipated and involved us reworking both how we mounted the exciter on the base and how the rod, which extended from the exciter, was supported and attached. 


Initially, the exciter rested on bolts which were set on machine screws an inch or two above the plywood base. In this setup, not only was it difficult to get the machine screws sufficiently straight so that the exciter could comfortably slide along them, but it was also hard to get the bolts set consistently at the right height so that the exciter was set level. This problem had a pleasantly simple solution: mount the exciter (vertically) as close to the base as possible. We did this by cutting an appropriately sized hole with a jigsaw in plywood, drilling painfully precise holes for the screws, and fitting the exciter right in. The exciter is buffered a little bit from the base by bolts, which have no play to screw (get it?) up the alignment. 


Slightly more difficult were the problems with how we the carriagle bolt, which connects the plate to the exciter, is attached to the exciter. Our first attempt involved cutting about an inch-long section of dowel, drilling a hole through that, sticking the bolt through it, and then attaching it to the exciter with some adhesive. This worked OK for our first few runs, but difficultly in drilling precisely straight through the dowel and to cutting its ends level manifested in an unlevel plate and biased patterns. 


For our second attempt, we replaced the dowel with a metal washer which promised to solve both issues. Unfortunately, we overlooked the fact that the exciter is driven by a magnet, and predictably the close proximity of the washer dampened its effect and eventually caused to its early demise. 

In what would be our final attempt (third time's the charm!), we used a 3/4" PVC endcap to raise the end of the bolt about an inch above the exciter. I drilled a hole slightly larger than necessary through the end and stuck a washer in tandem with the bolt on the inside end so that adjusting the angle at which the bolt exited the cap is possible. A wingnut slides screws over the bolt to clamp everything down and once everything was found to be nice and level, we attached the PVC to the exciter with some epoxy.

Finally, comes the issue of stabilizing the bolt. Even though we'd gotten the exciter and bolt level by themselves in static distuations, the mass distribution of the bolt/plate were such that any imperfection would again cause tilting one way or another. And imperfections there were plenty! Rather than waste our time trying to align centers of mass, we built the following device to stabilize the bolt as it moves up and down. 


It's design is pretty simple, and I'm kind of proud of it. It's probably the most magnificent thing I've ever built. The black part is a 3" to 2" PVC reduce with a rectangular hole cut in it for access to the exicter's terminals. On the 2" end, we hooked it up to an appropriately sized bushing that had a small 1/2" hole which we were able to glue a washer to. By some miracle, we had a pen shaft the both fit perfectly into the washer AND enclosed the carriage bolt, making for an excellent guide. We used a bit of dry lube to faciliate a more pleasurable interaction between the guide shaft and carriage bolt. We attached this whole assembly to the base via some dubiously gotten angle brackets. These were placed and screwed down so that they held the stabilizer on by friction, which allowed us to remove it as we placed and fiddle with the exciter when necessary.

Cutting the plates was probably the most creative part of this project. Paul and Sam measured and cut a square (or two), a circle (or two), and a triangle to test on the VIBRATINATOR 3000. These were mounted on the carriage bolt with a nut supporting it on the bottom and another one clamping it from the top. We put some black spray paint on the plates to set some contrast between them and the salt that would indicate the nodal lines.





## Results and Analysis
We got a lot of pretty pictures:
![alt text](https://github.com/salcott01/Chladni_Project/blob/main/IMG_8142.jpg)
So sensual...
![alt text](https://github.com/salcott01/Chladni_Project/blob/main/IMG_8143.jpg)
### Our Hypothesis
Because we're dealing with sound and vibrating plates, the wave equation immediately comes to mind as a suitable mathematical model. So why not model the plates in this way, and see if they hold up to that theory? [Here](https://github.com/salcott01/Chladni_Project/blob/main/thry.pdf) I've attached a short 3-page summary on the theory behind these driven vibrations. Based on this theory, we expect to find our first resonant frequency at about 7000 Hz (the speed of sound in shear aluminum is apparently ~3000 m/s)---noticeably disparate from the the first frequency at which we were able to observe nodal lines (around 200 Hz). And indeed, aluminum plates host a few characteristics that prevent them from being treated as an 2D membrane, thus making the wave equation an unapt descriptor. Probably the most damning of them all is the fact that aluminun is quite rigid and vibration causes motion along all axes at each point, leaving it best characterized by some combination of wave and material deformation.
### A Correction
Some research on this topic confirms that the vibration is indeed not described sufficiently by the wave equation, but rather by the fourth-order Kirchoff equation

![alt text](https://github.com/salcott01/Chladni_Project/blob/main/test.png)

Unfortunately, this has no analytic solutions applicable to square/circular plates and the normal modes must be calculated numerically. In fact, this problem applied to the plate so troubling that Rayleigh, an expert in this study at the time, described it as one "one of great difficulty, and [one which] has for the most part resisted attack," though it was eventually solved by Ritz numerically in the 1850s. I have neither the time or interest in learning how this is done, so I refer those interested to this article [here](http://www.unige.ch/~gander/Preprints/Ritz.pdf). 
