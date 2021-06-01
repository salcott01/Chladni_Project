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

Possibly the biggest obstacle in out building process was getting the darn plate level so the salt wouldn't pile off once we turned the exciter on.  

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

Unfortunately, this has no analytic solutions applicable to square/circular plates and the normal modes must be calculated numerically. In fact, this problem applied to the plate was so troubling that Rayleigh, an expert in this study at the time, described it as one "one of great difficulty, and [one which] has for the most part resisted attack," though it was eventually solved by Ritz numerically in the 1850s. I have neither the time or interest in learning how this is done, so I refer those interested to this article [here](http://www.unige.ch/~gander/Preprints/Ritz.pdf). 
