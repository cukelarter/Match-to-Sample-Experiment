#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on May 30, 2022, at 11:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'MatchToSample'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\cukel\\OneDrive\\Documents\\upwork\\PsychoPy_DDRTraining\\teaching_videovstext\\MatchToSample\\MatchToSample_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_instructions = event.Mouse(win=win)
x, y = [None, None]
mouse_instructions.mouseClock = core.Clock()

# Initialize components for Routine "observation"
observationClock = core.Clock()
sample_observation = visual.ImageStim(
    win=win,
    name='sample_observation', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_observation = event.Mouse(win=win)
x, y = [None, None]
mouse_observation.mouseClock = core.Clock()

# Initialize components for Routine "comparison"
comparisonClock = core.Clock()
sample_comparison = visual.ImageStim(
    win=win,
    name='sample_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_comparison = event.Mouse(win=win)
x, y = [None, None]
mouse_comparison.mouseClock = core.Clock()
stim1_comparison = visual.ImageStim(
    win=win,
    name='stim1_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.4,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
stim2_comparison = visual.ImageStim(
    win=win,
    name='stim2_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
stim3_comparison = visual.ImageStim(
    win=win,
    name='stim3_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0.4,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
correcttrials=0
totaltrials=0
mastery_criteria=0

# Initialize components for Routine "reset_count"
reset_countClock = core.Clock()
text_startblock = visual.TextStim(win=win, name='text_startblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "observation"
observationClock = core.Clock()
sample_observation = visual.ImageStim(
    win=win,
    name='sample_observation', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_observation = event.Mouse(win=win)
x, y = [None, None]
mouse_observation.mouseClock = core.Clock()

# Initialize components for Routine "comparison"
comparisonClock = core.Clock()
sample_comparison = visual.ImageStim(
    win=win,
    name='sample_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_comparison = event.Mouse(win=win)
x, y = [None, None]
mouse_comparison.mouseClock = core.Clock()
stim1_comparison = visual.ImageStim(
    win=win,
    name='stim1_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.4,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
stim2_comparison = visual.ImageStim(
    win=win,
    name='stim2_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
stim3_comparison = visual.ImageStim(
    win=win,
    name='stim3_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0.4,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
correcttrials=0
totaltrials=0
mastery_criteria=0

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "block_feedback"
block_feedbackClock = core.Clock()
text_blockfeedback = visual.TextStim(win=win, name='text_blockfeedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_blockfeedback = event.Mouse(win=win)
x, y = [None, None]
mouse_blockfeedback.mouseClock = core.Clock()

# Initialize components for Routine "reset_count"
reset_countClock = core.Clock()
text_startblock = visual.TextStim(win=win, name='text_startblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "observation"
observationClock = core.Clock()
sample_observation = visual.ImageStim(
    win=win,
    name='sample_observation', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_observation = event.Mouse(win=win)
x, y = [None, None]
mouse_observation.mouseClock = core.Clock()

# Initialize components for Routine "comparison"
comparisonClock = core.Clock()
sample_comparison = visual.ImageStim(
    win=win,
    name='sample_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_comparison = event.Mouse(win=win)
x, y = [None, None]
mouse_comparison.mouseClock = core.Clock()
stim1_comparison = visual.ImageStim(
    win=win,
    name='stim1_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.4,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
stim2_comparison = visual.ImageStim(
    win=win,
    name='stim2_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
stim3_comparison = visual.ImageStim(
    win=win,
    name='stim3_comparison', 
    image='sin', mask=None,
    ori=0.0, pos=(0.4,-0.26), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
correcttrials=0
totaltrials=0
mastery_criteria=0

# Initialize components for Routine "block_feedback_posttest"
block_feedback_posttestClock = core.Clock()
text_blockfeedback_2 = visual.TextStim(win=win, name='text_blockfeedback_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_blockfeedback_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_blockfeedback_2.mouseClock = core.Clock()

# Initialize components for Routine "check_posttest"
check_posttestClock = core.Clock()
text_posttest = visual.TextStim(win=win, name='text_posttest',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_instructions = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('excel/instructions.xlsx'),
    seed=None, name='trials_instructions')
thisExp.addLoop(trials_instructions)  # add the loop to the experiment
thisTrials_instruction = trials_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_instruction.rgb)
if thisTrials_instruction != None:
    for paramName in thisTrials_instruction:
        exec('{} = thisTrials_instruction[paramName]'.format(paramName))

for thisTrials_instruction in trials_instructions:
    currentLoop = trials_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_instruction.rgb)
    if thisTrials_instruction != None:
        for paramName in thisTrials_instruction:
            exec('{} = thisTrials_instruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_instructions.setText(instr1)
    # setup some python lists for storing info about the mouse_instructions
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionsComponents = [text_instructions, mouse_instructions]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instructions* updates
        if text_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instructions.frameNStart = frameN  # exact frame index
            text_instructions.tStart = t  # local t and not account for scr refresh
            text_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instructions, 'tStartRefresh')  # time at next scr refresh
            text_instructions.setAutoDraw(True)
        # *mouse_instructions* updates
        if mouse_instructions.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_instructions.frameNStart = frameN  # exact frame index
            mouse_instructions.tStart = t  # local t and not account for scr refresh
            mouse_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_instructions, 'tStartRefresh')  # time at next scr refresh
            mouse_instructions.status = STARTED
            mouse_instructions.mouseClock.reset()
            prevButtonState = mouse_instructions.getPressed()  # if button is down already this ISN'T a new click
        if mouse_instructions.status == STARTED:  # only update if started and not finished!
            buttons = mouse_instructions.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_instructions.addData('text_instructions.started', text_instructions.tStartRefresh)
    trials_instructions.addData('text_instructions.stopped', text_instructions.tStopRefresh)
    # store data for trials_instructions (TrialHandler)
    x, y = mouse_instructions.getPos()
    buttons = mouse_instructions.getPressed()
    trials_instructions.addData('mouse_instructions.x', x)
    trials_instructions.addData('mouse_instructions.y', y)
    trials_instructions.addData('mouse_instructions.leftButton', buttons[0])
    trials_instructions.addData('mouse_instructions.midButton', buttons[1])
    trials_instructions.addData('mouse_instructions.rightButton', buttons[2])
    trials_instructions.addData('mouse_instructions.started', mouse_instructions.tStart)
    trials_instructions.addData('mouse_instructions.stopped', mouse_instructions.tStop)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_instructions'


# set up handler to look after randomisation of conditions etc
block_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('excel/pretest_blocktable.xlsx'),
    seed=None, name='block_loop')
thisExp.addLoop(block_loop)  # add the loop to the experiment
thisBlock_loop = block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop:
        exec('{} = thisBlock_loop[paramName]'.format(paramName))

for thisBlock_loop in block_loop:
    currentLoop = block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop:
            exec('{} = thisBlock_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_pretest = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CueTbl),
        seed=None, name='trials_pretest')
    thisExp.addLoop(trials_pretest)  # add the loop to the experiment
    thisTrials_pretest = trials_pretest.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_pretest.rgb)
    if thisTrials_pretest != None:
        for paramName in thisTrials_pretest:
            exec('{} = thisTrials_pretest[paramName]'.format(paramName))
    
    for thisTrials_pretest in trials_pretest:
        currentLoop = trials_pretest
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_pretest.rgb)
        if thisTrials_pretest != None:
            for paramName in thisTrials_pretest:
                exec('{} = thisTrials_pretest[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "observation"-------
        continueRoutine = True
        # update component parameters for each repeat
        sample_observation.setImage(Sample)
        # setup some python lists for storing info about the mouse_observation
        mouse_observation.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        observationComponents = [sample_observation, mouse_observation]
        for thisComponent in observationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        observationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "observation"-------
        while continueRoutine:
            # get current time
            t = observationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=observationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sample_observation* updates
            if sample_observation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sample_observation.frameNStart = frameN  # exact frame index
                sample_observation.tStart = t  # local t and not account for scr refresh
                sample_observation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sample_observation, 'tStartRefresh')  # time at next scr refresh
                sample_observation.setAutoDraw(True)
            # *mouse_observation* updates
            if mouse_observation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_observation.frameNStart = frameN  # exact frame index
                mouse_observation.tStart = t  # local t and not account for scr refresh
                mouse_observation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_observation, 'tStartRefresh')  # time at next scr refresh
                mouse_observation.status = STARTED
                mouse_observation.mouseClock.reset()
                prevButtonState = mouse_observation.getPressed()  # if button is down already this ISN'T a new click
            if mouse_observation.status == STARTED:  # only update if started and not finished!
                buttons = mouse_observation.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [sample_observation]:
                            if obj.contains(mouse_observation):
                                gotValidClick = True
                                mouse_observation.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in observationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "observation"-------
        for thisComponent in observationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_pretest.addData('sample_observation.started', sample_observation.tStartRefresh)
        trials_pretest.addData('sample_observation.stopped', sample_observation.tStopRefresh)
        # store data for trials_pretest (TrialHandler)
        x, y = mouse_observation.getPos()
        buttons = mouse_observation.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [sample_observation]:
                if obj.contains(mouse_observation):
                    gotValidClick = True
                    mouse_observation.clicked_name.append(obj.name)
        trials_pretest.addData('mouse_observation.x', x)
        trials_pretest.addData('mouse_observation.y', y)
        trials_pretest.addData('mouse_observation.leftButton', buttons[0])
        trials_pretest.addData('mouse_observation.midButton', buttons[1])
        trials_pretest.addData('mouse_observation.rightButton', buttons[2])
        if len(mouse_observation.clicked_name):
            trials_pretest.addData('mouse_observation.clicked_name', mouse_observation.clicked_name[0])
        trials_pretest.addData('mouse_observation.started', mouse_observation.tStart)
        trials_pretest.addData('mouse_observation.stopped', mouse_observation.tStop)
        # the Routine "observation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "comparison"-------
        continueRoutine = True
        # update component parameters for each repeat
        sample_comparison.setImage(Sample)
        # setup some python lists for storing info about the mouse_comparison
        mouse_comparison.clicked_name = []
        gotValidClick = False  # until a click is received
        stim1_comparison.setImage(stim1)
        stim2_comparison.setImage(stim2)
        stim3_comparison.setImage(stim3)
        # keep track of which components have finished
        comparisonComponents = [sample_comparison, mouse_comparison, stim1_comparison, stim2_comparison, stim3_comparison]
        for thisComponent in comparisonComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        comparisonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "comparison"-------
        while continueRoutine:
            # get current time
            t = comparisonClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=comparisonClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sample_comparison* updates
            if sample_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sample_comparison.frameNStart = frameN  # exact frame index
                sample_comparison.tStart = t  # local t and not account for scr refresh
                sample_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sample_comparison, 'tStartRefresh')  # time at next scr refresh
                sample_comparison.setAutoDraw(True)
            # *mouse_comparison* updates
            if mouse_comparison.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_comparison.frameNStart = frameN  # exact frame index
                mouse_comparison.tStart = t  # local t and not account for scr refresh
                mouse_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_comparison, 'tStartRefresh')  # time at next scr refresh
                mouse_comparison.status = STARTED
                mouse_comparison.mouseClock.reset()
                prevButtonState = mouse_comparison.getPressed()  # if button is down already this ISN'T a new click
            if mouse_comparison.status == STARTED:  # only update if started and not finished!
                buttons = mouse_comparison.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [stim1_comparison,stim2_comparison,stim3_comparison]:
                            if obj.contains(mouse_comparison):
                                gotValidClick = True
                                mouse_comparison.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *stim1_comparison* updates
            if stim1_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim1_comparison.frameNStart = frameN  # exact frame index
                stim1_comparison.tStart = t  # local t and not account for scr refresh
                stim1_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim1_comparison, 'tStartRefresh')  # time at next scr refresh
                stim1_comparison.setAutoDraw(True)
            
            # *stim2_comparison* updates
            if stim2_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim2_comparison.frameNStart = frameN  # exact frame index
                stim2_comparison.tStart = t  # local t and not account for scr refresh
                stim2_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim2_comparison, 'tStartRefresh')  # time at next scr refresh
                stim2_comparison.setAutoDraw(True)
            
            # *stim3_comparison* updates
            if stim3_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim3_comparison.frameNStart = frameN  # exact frame index
                stim3_comparison.tStart = t  # local t and not account for scr refresh
                stim3_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim3_comparison, 'tStartRefresh')  # time at next scr refresh
                stim3_comparison.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in comparisonComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "comparison"-------
        for thisComponent in comparisonComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_pretest.addData('sample_comparison.started', sample_comparison.tStartRefresh)
        trials_pretest.addData('sample_comparison.stopped', sample_comparison.tStopRefresh)
        # store data for trials_pretest (TrialHandler)
        x, y = mouse_comparison.getPos()
        buttons = mouse_comparison.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [stim1_comparison,stim2_comparison,stim3_comparison]:
                if obj.contains(mouse_comparison):
                    gotValidClick = True
                    mouse_comparison.clicked_name.append(obj.name)
        trials_pretest.addData('mouse_comparison.x', x)
        trials_pretest.addData('mouse_comparison.y', y)
        trials_pretest.addData('mouse_comparison.leftButton', buttons[0])
        trials_pretest.addData('mouse_comparison.midButton', buttons[1])
        trials_pretest.addData('mouse_comparison.rightButton', buttons[2])
        if len(mouse_comparison.clicked_name):
            trials_pretest.addData('mouse_comparison.clicked_name', mouse_comparison.clicked_name[0])
        trials_pretest.addData('mouse_comparison.started', mouse_comparison.tStart)
        trials_pretest.addData('mouse_comparison.stopped', mouse_comparison.tStop)
        trials_pretest.addData('stim1_comparison.started', stim1_comparison.tStartRefresh)
        trials_pretest.addData('stim1_comparison.stopped', stim1_comparison.tStopRefresh)
        trials_pretest.addData('stim2_comparison.started', stim2_comparison.tStartRefresh)
        trials_pretest.addData('stim2_comparison.stopped', stim2_comparison.tStopRefresh)
        trials_pretest.addData('stim3_comparison.started', stim3_comparison.tStartRefresh)
        trials_pretest.addData('stim3_comparison.stopped', stim3_comparison.tStopRefresh)
        clickedname=mouse_comparison.clicked_name[0].split('_')[0] 
        # clickedname = "stim1" OR "stim2" OR "stim3"
        # ".split(..." removes suffix from name
        thisExp.addData('clickedname',clickedname)
        # add it to our output data
        
        trialcorrect=clickedname==correctstim
        # trialcorrect = TRUE (1) or FALSE (0)
        # compare the clicked element to the correct stim provided by CueTbl
        thisExp.addData('trialcorrect',trialcorrect)
        # add it to our output data
        
        # update trial counters
        correcttrials+=trialcorrect # (1 or 0)
        totaltrials+=1
        
        # control feedback message
        if trialcorrect:
            msg_feedback=f"Correct! Nice Job! \n You got {str(correcttrials)} out of {str(totaltrials)} correct!"
        else:
            msg_feedback="Try Again!"
         
        accuracy=correcttrials/totaltrials
        # get accuracy to compare against mastery criteria
        
        passedBlock=accuracy>=mastery_criteria
        # passedBlock = TRUE (1) or FALSE (0)
        # if accuracy is over mastery criteria, they passed
        
        thisExp.addData('passedBlock',passedBlock)
        # record whether or not participant passed the block
        
        # control block feedback message
        if passedBlock:
            msg_blockfeedback=f"You passed that block! Nice job!"
            # populate a passed/good message
        else:
            msg_blockfeedback=f"You failed that block! Try Again!"
            # populate a failed/bad message
        
        
        # the Routine "comparison" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_pretest'
    
# completed 1.0 repeats of 'block_loop'


# set up handler to look after randomisation of conditions etc
repeat_task = data.TrialHandler(nReps=50.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeat_task')
thisExp.addLoop(repeat_task)  # add the loop to the experiment
thisRepeat_task = repeat_task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat_task.rgb)
if thisRepeat_task != None:
    for paramName in thisRepeat_task:
        exec('{} = thisRepeat_task[paramName]'.format(paramName))

for thisRepeat_task in repeat_task:
    currentLoop = repeat_task
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_task.rgb)
    if thisRepeat_task != None:
        for paramName in thisRepeat_task:
            exec('{} = thisRepeat_task[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    block_training = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('excel/training_blocktable.xlsx'),
        seed=None, name='block_training')
    thisExp.addLoop(block_training)  # add the loop to the experiment
    thisBlock_training = block_training.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_training.rgb)
    if thisBlock_training != None:
        for paramName in thisBlock_training:
            exec('{} = thisBlock_training[paramName]'.format(paramName))
    
    for thisBlock_training in block_training:
        currentLoop = block_training
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_training.rgb)
        if thisBlock_training != None:
            for paramName in thisBlock_training:
                exec('{} = thisBlock_training[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        repeat_block = data.TrialHandler(nReps=50.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='repeat_block')
        thisExp.addLoop(repeat_block)  # add the loop to the experiment
        thisRepeat_block = repeat_block.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat_block.rgb)
        if thisRepeat_block != None:
            for paramName in thisRepeat_block:
                exec('{} = thisRepeat_block[paramName]'.format(paramName))
        
        for thisRepeat_block in repeat_block:
            currentLoop = repeat_block
            # abbreviate parameter names if possible (e.g. rgb = thisRepeat_block.rgb)
            if thisRepeat_block != None:
                for paramName in thisRepeat_block:
                    exec('{} = thisRepeat_block[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "reset_count"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            text_startblock.setText(BlockMessage)
            # keep track of which components have finished
            reset_countComponents = [text_startblock]
            for thisComponent in reset_countComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            reset_countClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "reset_count"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = reset_countClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=reset_countClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_startblock* updates
                if text_startblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_startblock.frameNStart = frameN  # exact frame index
                    text_startblock.tStart = t  # local t and not account for scr refresh
                    text_startblock.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_startblock, 'tStartRefresh')  # time at next scr refresh
                    text_startblock.setAutoDraw(True)
                if text_startblock.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_startblock.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_startblock.tStop = t  # not accounting for scr refresh
                        text_startblock.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_startblock, 'tStopRefresh')  # time at next scr refresh
                        text_startblock.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in reset_countComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "reset_count"-------
            for thisComponent in reset_countComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            repeat_block.addData('text_startblock.started', text_startblock.tStartRefresh)
            repeat_block.addData('text_startblock.stopped', text_startblock.tStopRefresh)
            correcttrials=0
            totaltrials=0
            
            # set up handler to look after randomisation of conditions etc
            trials_training = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(CueTbl),
                seed=None, name='trials_training')
            thisExp.addLoop(trials_training)  # add the loop to the experiment
            thisTrials_training = trials_training.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_training.rgb)
            if thisTrials_training != None:
                for paramName in thisTrials_training:
                    exec('{} = thisTrials_training[paramName]'.format(paramName))
            
            for thisTrials_training in trials_training:
                currentLoop = trials_training
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_training.rgb)
                if thisTrials_training != None:
                    for paramName in thisTrials_training:
                        exec('{} = thisTrials_training[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "observation"-------
                continueRoutine = True
                # update component parameters for each repeat
                sample_observation.setImage(Sample)
                # setup some python lists for storing info about the mouse_observation
                mouse_observation.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                observationComponents = [sample_observation, mouse_observation]
                for thisComponent in observationComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                observationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "observation"-------
                while continueRoutine:
                    # get current time
                    t = observationClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=observationClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *sample_observation* updates
                    if sample_observation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        sample_observation.frameNStart = frameN  # exact frame index
                        sample_observation.tStart = t  # local t and not account for scr refresh
                        sample_observation.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(sample_observation, 'tStartRefresh')  # time at next scr refresh
                        sample_observation.setAutoDraw(True)
                    # *mouse_observation* updates
                    if mouse_observation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_observation.frameNStart = frameN  # exact frame index
                        mouse_observation.tStart = t  # local t and not account for scr refresh
                        mouse_observation.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_observation, 'tStartRefresh')  # time at next scr refresh
                        mouse_observation.status = STARTED
                        mouse_observation.mouseClock.reset()
                        prevButtonState = mouse_observation.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_observation.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_observation.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                for obj in [sample_observation]:
                                    if obj.contains(mouse_observation):
                                        gotValidClick = True
                                        mouse_observation.clicked_name.append(obj.name)
                                if gotValidClick:  # abort routine on response
                                    continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in observationComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "observation"-------
                for thisComponent in observationComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials_training.addData('sample_observation.started', sample_observation.tStartRefresh)
                trials_training.addData('sample_observation.stopped', sample_observation.tStopRefresh)
                # store data for trials_training (TrialHandler)
                x, y = mouse_observation.getPos()
                buttons = mouse_observation.getPressed()
                if sum(buttons):
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [sample_observation]:
                        if obj.contains(mouse_observation):
                            gotValidClick = True
                            mouse_observation.clicked_name.append(obj.name)
                trials_training.addData('mouse_observation.x', x)
                trials_training.addData('mouse_observation.y', y)
                trials_training.addData('mouse_observation.leftButton', buttons[0])
                trials_training.addData('mouse_observation.midButton', buttons[1])
                trials_training.addData('mouse_observation.rightButton', buttons[2])
                if len(mouse_observation.clicked_name):
                    trials_training.addData('mouse_observation.clicked_name', mouse_observation.clicked_name[0])
                trials_training.addData('mouse_observation.started', mouse_observation.tStart)
                trials_training.addData('mouse_observation.stopped', mouse_observation.tStop)
                # the Routine "observation" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "comparison"-------
                continueRoutine = True
                # update component parameters for each repeat
                sample_comparison.setImage(Sample)
                # setup some python lists for storing info about the mouse_comparison
                mouse_comparison.clicked_name = []
                gotValidClick = False  # until a click is received
                stim1_comparison.setImage(stim1)
                stim2_comparison.setImage(stim2)
                stim3_comparison.setImage(stim3)
                # keep track of which components have finished
                comparisonComponents = [sample_comparison, mouse_comparison, stim1_comparison, stim2_comparison, stim3_comparison]
                for thisComponent in comparisonComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                comparisonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "comparison"-------
                while continueRoutine:
                    # get current time
                    t = comparisonClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=comparisonClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *sample_comparison* updates
                    if sample_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        sample_comparison.frameNStart = frameN  # exact frame index
                        sample_comparison.tStart = t  # local t and not account for scr refresh
                        sample_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(sample_comparison, 'tStartRefresh')  # time at next scr refresh
                        sample_comparison.setAutoDraw(True)
                    # *mouse_comparison* updates
                    if mouse_comparison.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_comparison.frameNStart = frameN  # exact frame index
                        mouse_comparison.tStart = t  # local t and not account for scr refresh
                        mouse_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_comparison, 'tStartRefresh')  # time at next scr refresh
                        mouse_comparison.status = STARTED
                        mouse_comparison.mouseClock.reset()
                        prevButtonState = mouse_comparison.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_comparison.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_comparison.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                for obj in [stim1_comparison,stim2_comparison,stim3_comparison]:
                                    if obj.contains(mouse_comparison):
                                        gotValidClick = True
                                        mouse_comparison.clicked_name.append(obj.name)
                                if gotValidClick:  # abort routine on response
                                    continueRoutine = False
                    
                    # *stim1_comparison* updates
                    if stim1_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim1_comparison.frameNStart = frameN  # exact frame index
                        stim1_comparison.tStart = t  # local t and not account for scr refresh
                        stim1_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim1_comparison, 'tStartRefresh')  # time at next scr refresh
                        stim1_comparison.setAutoDraw(True)
                    
                    # *stim2_comparison* updates
                    if stim2_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim2_comparison.frameNStart = frameN  # exact frame index
                        stim2_comparison.tStart = t  # local t and not account for scr refresh
                        stim2_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim2_comparison, 'tStartRefresh')  # time at next scr refresh
                        stim2_comparison.setAutoDraw(True)
                    
                    # *stim3_comparison* updates
                    if stim3_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim3_comparison.frameNStart = frameN  # exact frame index
                        stim3_comparison.tStart = t  # local t and not account for scr refresh
                        stim3_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim3_comparison, 'tStartRefresh')  # time at next scr refresh
                        stim3_comparison.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in comparisonComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "comparison"-------
                for thisComponent in comparisonComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials_training.addData('sample_comparison.started', sample_comparison.tStartRefresh)
                trials_training.addData('sample_comparison.stopped', sample_comparison.tStopRefresh)
                # store data for trials_training (TrialHandler)
                x, y = mouse_comparison.getPos()
                buttons = mouse_comparison.getPressed()
                if sum(buttons):
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [stim1_comparison,stim2_comparison,stim3_comparison]:
                        if obj.contains(mouse_comparison):
                            gotValidClick = True
                            mouse_comparison.clicked_name.append(obj.name)
                trials_training.addData('mouse_comparison.x', x)
                trials_training.addData('mouse_comparison.y', y)
                trials_training.addData('mouse_comparison.leftButton', buttons[0])
                trials_training.addData('mouse_comparison.midButton', buttons[1])
                trials_training.addData('mouse_comparison.rightButton', buttons[2])
                if len(mouse_comparison.clicked_name):
                    trials_training.addData('mouse_comparison.clicked_name', mouse_comparison.clicked_name[0])
                trials_training.addData('mouse_comparison.started', mouse_comparison.tStart)
                trials_training.addData('mouse_comparison.stopped', mouse_comparison.tStop)
                trials_training.addData('stim1_comparison.started', stim1_comparison.tStartRefresh)
                trials_training.addData('stim1_comparison.stopped', stim1_comparison.tStopRefresh)
                trials_training.addData('stim2_comparison.started', stim2_comparison.tStartRefresh)
                trials_training.addData('stim2_comparison.stopped', stim2_comparison.tStopRefresh)
                trials_training.addData('stim3_comparison.started', stim3_comparison.tStartRefresh)
                trials_training.addData('stim3_comparison.stopped', stim3_comparison.tStopRefresh)
                clickedname=mouse_comparison.clicked_name[0].split('_')[0] 
                # clickedname = "stim1" OR "stim2" OR "stim3"
                # ".split(..." removes suffix from name
                thisExp.addData('clickedname',clickedname)
                # add it to our output data
                
                trialcorrect=clickedname==correctstim
                # trialcorrect = TRUE (1) or FALSE (0)
                # compare the clicked element to the correct stim provided by CueTbl
                thisExp.addData('trialcorrect',trialcorrect)
                # add it to our output data
                
                # update trial counters
                correcttrials+=trialcorrect # (1 or 0)
                totaltrials+=1
                
                # control feedback message
                if trialcorrect:
                    msg_feedback=f"Correct! Nice Job! \n You got {str(correcttrials)} out of {str(totaltrials)} correct!"
                else:
                    msg_feedback="Try Again!"
                 
                accuracy=correcttrials/totaltrials
                # get accuracy to compare against mastery criteria
                
                passedBlock=accuracy>=mastery_criteria
                # passedBlock = TRUE (1) or FALSE (0)
                # if accuracy is over mastery criteria, they passed
                
                thisExp.addData('passedBlock',passedBlock)
                # record whether or not participant passed the block
                
                # control block feedback message
                if passedBlock:
                    msg_blockfeedback=f"You passed that block! Nice job!"
                    # populate a passed/good message
                else:
                    msg_blockfeedback=f"You failed that block! Try Again!"
                    # populate a failed/bad message
                
                
                # the Routine "comparison" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "feedback"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                text_feedback.setText(msg_feedback)
                # keep track of which components have finished
                feedbackComponents = [text_feedback]
                for thisComponent in feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "feedback"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = feedbackClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_feedback* updates
                    if text_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_feedback.frameNStart = frameN  # exact frame index
                        text_feedback.tStart = t  # local t and not account for scr refresh
                        text_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_feedback, 'tStartRefresh')  # time at next scr refresh
                        text_feedback.setAutoDraw(True)
                    if text_feedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_feedback.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            text_feedback.tStop = t  # not accounting for scr refresh
                            text_feedback.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_feedback, 'tStopRefresh')  # time at next scr refresh
                            text_feedback.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "feedback"-------
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                trials_training.addData('text_feedback.started', text_feedback.tStartRefresh)
                trials_training.addData('text_feedback.stopped', text_feedback.tStopRefresh)
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'trials_training'
            
            
            # ------Prepare to start Routine "block_feedback"-------
            continueRoutine = True
            # update component parameters for each repeat
            text_blockfeedback.setText(msg_blockfeedback)
            # setup some python lists for storing info about the mouse_blockfeedback
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            block_feedbackComponents = [text_blockfeedback, mouse_blockfeedback]
            for thisComponent in block_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            block_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "block_feedback"-------
            while continueRoutine:
                # get current time
                t = block_feedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=block_feedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_blockfeedback* updates
                if text_blockfeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_blockfeedback.frameNStart = frameN  # exact frame index
                    text_blockfeedback.tStart = t  # local t and not account for scr refresh
                    text_blockfeedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_blockfeedback, 'tStartRefresh')  # time at next scr refresh
                    text_blockfeedback.setAutoDraw(True)
                # *mouse_blockfeedback* updates
                if mouse_blockfeedback.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_blockfeedback.frameNStart = frameN  # exact frame index
                    mouse_blockfeedback.tStart = t  # local t and not account for scr refresh
                    mouse_blockfeedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_blockfeedback, 'tStartRefresh')  # time at next scr refresh
                    mouse_blockfeedback.status = STARTED
                    mouse_blockfeedback.mouseClock.reset()
                    prevButtonState = mouse_blockfeedback.getPressed()  # if button is down already this ISN'T a new click
                if mouse_blockfeedback.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_blockfeedback.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # abort routine on response
                            continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "block_feedback"-------
            for thisComponent in block_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            repeat_block.addData('text_blockfeedback.started', text_blockfeedback.tStartRefresh)
            repeat_block.addData('text_blockfeedback.stopped', text_blockfeedback.tStopRefresh)
            # store data for repeat_block (TrialHandler)
            x, y = mouse_blockfeedback.getPos()
            buttons = mouse_blockfeedback.getPressed()
            repeat_block.addData('mouse_blockfeedback.x', x)
            repeat_block.addData('mouse_blockfeedback.y', y)
            repeat_block.addData('mouse_blockfeedback.leftButton', buttons[0])
            repeat_block.addData('mouse_blockfeedback.midButton', buttons[1])
            repeat_block.addData('mouse_blockfeedback.rightButton', buttons[2])
            repeat_block.addData('mouse_blockfeedback.started', mouse_blockfeedback.tStart)
            repeat_block.addData('mouse_blockfeedback.stopped', mouse_blockfeedback.tStop)
            if passedBlock:
                repeat_block.finished=True
            # if the participant passes the previous block
            # then this will break us out of the "repeat_block" loop
            # otherwise it will continue to repeat
             
            
            # the Routine "block_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 50.0 repeats of 'repeat_block'
        
    # completed 1.0 repeats of 'block_training'
    
    
    # set up handler to look after randomisation of conditions etc
    block_posttest = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('excel/posttest_blocktable.xlsx'),
        seed=None, name='block_posttest')
    thisExp.addLoop(block_posttest)  # add the loop to the experiment
    thisBlock_posttest = block_posttest.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_posttest.rgb)
    if thisBlock_posttest != None:
        for paramName in thisBlock_posttest:
            exec('{} = thisBlock_posttest[paramName]'.format(paramName))
    
    for thisBlock_posttest in block_posttest:
        currentLoop = block_posttest
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_posttest.rgb)
        if thisBlock_posttest != None:
            for paramName in thisBlock_posttest:
                exec('{} = thisBlock_posttest[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "reset_count"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        text_startblock.setText(BlockMessage)
        # keep track of which components have finished
        reset_countComponents = [text_startblock]
        for thisComponent in reset_countComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        reset_countClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "reset_count"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = reset_countClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=reset_countClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_startblock* updates
            if text_startblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_startblock.frameNStart = frameN  # exact frame index
                text_startblock.tStart = t  # local t and not account for scr refresh
                text_startblock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_startblock, 'tStartRefresh')  # time at next scr refresh
                text_startblock.setAutoDraw(True)
            if text_startblock.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_startblock.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_startblock.tStop = t  # not accounting for scr refresh
                    text_startblock.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_startblock, 'tStopRefresh')  # time at next scr refresh
                    text_startblock.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_countComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "reset_count"-------
        for thisComponent in reset_countComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_posttest.addData('text_startblock.started', text_startblock.tStartRefresh)
        block_posttest.addData('text_startblock.stopped', text_startblock.tStopRefresh)
        correcttrials=0
        totaltrials=0
        
        # set up handler to look after randomisation of conditions etc
        trials_posttest = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(CueTbl),
            seed=None, name='trials_posttest')
        thisExp.addLoop(trials_posttest)  # add the loop to the experiment
        thisTrials_posttest = trials_posttest.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_posttest.rgb)
        if thisTrials_posttest != None:
            for paramName in thisTrials_posttest:
                exec('{} = thisTrials_posttest[paramName]'.format(paramName))
        
        for thisTrials_posttest in trials_posttest:
            currentLoop = trials_posttest
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_posttest.rgb)
            if thisTrials_posttest != None:
                for paramName in thisTrials_posttest:
                    exec('{} = thisTrials_posttest[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "observation"-------
            continueRoutine = True
            # update component parameters for each repeat
            sample_observation.setImage(Sample)
            # setup some python lists for storing info about the mouse_observation
            mouse_observation.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            observationComponents = [sample_observation, mouse_observation]
            for thisComponent in observationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            observationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "observation"-------
            while continueRoutine:
                # get current time
                t = observationClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=observationClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *sample_observation* updates
                if sample_observation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sample_observation.frameNStart = frameN  # exact frame index
                    sample_observation.tStart = t  # local t and not account for scr refresh
                    sample_observation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sample_observation, 'tStartRefresh')  # time at next scr refresh
                    sample_observation.setAutoDraw(True)
                # *mouse_observation* updates
                if mouse_observation.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_observation.frameNStart = frameN  # exact frame index
                    mouse_observation.tStart = t  # local t and not account for scr refresh
                    mouse_observation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_observation, 'tStartRefresh')  # time at next scr refresh
                    mouse_observation.status = STARTED
                    mouse_observation.mouseClock.reset()
                    prevButtonState = mouse_observation.getPressed()  # if button is down already this ISN'T a new click
                if mouse_observation.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_observation.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [sample_observation]:
                                if obj.contains(mouse_observation):
                                    gotValidClick = True
                                    mouse_observation.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in observationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "observation"-------
            for thisComponent in observationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_posttest.addData('sample_observation.started', sample_observation.tStartRefresh)
            trials_posttest.addData('sample_observation.stopped', sample_observation.tStopRefresh)
            # store data for trials_posttest (TrialHandler)
            x, y = mouse_observation.getPos()
            buttons = mouse_observation.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [sample_observation]:
                    if obj.contains(mouse_observation):
                        gotValidClick = True
                        mouse_observation.clicked_name.append(obj.name)
            trials_posttest.addData('mouse_observation.x', x)
            trials_posttest.addData('mouse_observation.y', y)
            trials_posttest.addData('mouse_observation.leftButton', buttons[0])
            trials_posttest.addData('mouse_observation.midButton', buttons[1])
            trials_posttest.addData('mouse_observation.rightButton', buttons[2])
            if len(mouse_observation.clicked_name):
                trials_posttest.addData('mouse_observation.clicked_name', mouse_observation.clicked_name[0])
            trials_posttest.addData('mouse_observation.started', mouse_observation.tStart)
            trials_posttest.addData('mouse_observation.stopped', mouse_observation.tStop)
            # the Routine "observation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "comparison"-------
            continueRoutine = True
            # update component parameters for each repeat
            sample_comparison.setImage(Sample)
            # setup some python lists for storing info about the mouse_comparison
            mouse_comparison.clicked_name = []
            gotValidClick = False  # until a click is received
            stim1_comparison.setImage(stim1)
            stim2_comparison.setImage(stim2)
            stim3_comparison.setImage(stim3)
            # keep track of which components have finished
            comparisonComponents = [sample_comparison, mouse_comparison, stim1_comparison, stim2_comparison, stim3_comparison]
            for thisComponent in comparisonComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            comparisonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "comparison"-------
            while continueRoutine:
                # get current time
                t = comparisonClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=comparisonClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *sample_comparison* updates
                if sample_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sample_comparison.frameNStart = frameN  # exact frame index
                    sample_comparison.tStart = t  # local t and not account for scr refresh
                    sample_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sample_comparison, 'tStartRefresh')  # time at next scr refresh
                    sample_comparison.setAutoDraw(True)
                # *mouse_comparison* updates
                if mouse_comparison.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_comparison.frameNStart = frameN  # exact frame index
                    mouse_comparison.tStart = t  # local t and not account for scr refresh
                    mouse_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_comparison, 'tStartRefresh')  # time at next scr refresh
                    mouse_comparison.status = STARTED
                    mouse_comparison.mouseClock.reset()
                    prevButtonState = mouse_comparison.getPressed()  # if button is down already this ISN'T a new click
                if mouse_comparison.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_comparison.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [stim1_comparison,stim2_comparison,stim3_comparison]:
                                if obj.contains(mouse_comparison):
                                    gotValidClick = True
                                    mouse_comparison.clicked_name.append(obj.name)
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # *stim1_comparison* updates
                if stim1_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim1_comparison.frameNStart = frameN  # exact frame index
                    stim1_comparison.tStart = t  # local t and not account for scr refresh
                    stim1_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim1_comparison, 'tStartRefresh')  # time at next scr refresh
                    stim1_comparison.setAutoDraw(True)
                
                # *stim2_comparison* updates
                if stim2_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim2_comparison.frameNStart = frameN  # exact frame index
                    stim2_comparison.tStart = t  # local t and not account for scr refresh
                    stim2_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim2_comparison, 'tStartRefresh')  # time at next scr refresh
                    stim2_comparison.setAutoDraw(True)
                
                # *stim3_comparison* updates
                if stim3_comparison.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim3_comparison.frameNStart = frameN  # exact frame index
                    stim3_comparison.tStart = t  # local t and not account for scr refresh
                    stim3_comparison.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim3_comparison, 'tStartRefresh')  # time at next scr refresh
                    stim3_comparison.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comparisonComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "comparison"-------
            for thisComponent in comparisonComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_posttest.addData('sample_comparison.started', sample_comparison.tStartRefresh)
            trials_posttest.addData('sample_comparison.stopped', sample_comparison.tStopRefresh)
            # store data for trials_posttest (TrialHandler)
            x, y = mouse_comparison.getPos()
            buttons = mouse_comparison.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [stim1_comparison,stim2_comparison,stim3_comparison]:
                    if obj.contains(mouse_comparison):
                        gotValidClick = True
                        mouse_comparison.clicked_name.append(obj.name)
            trials_posttest.addData('mouse_comparison.x', x)
            trials_posttest.addData('mouse_comparison.y', y)
            trials_posttest.addData('mouse_comparison.leftButton', buttons[0])
            trials_posttest.addData('mouse_comparison.midButton', buttons[1])
            trials_posttest.addData('mouse_comparison.rightButton', buttons[2])
            if len(mouse_comparison.clicked_name):
                trials_posttest.addData('mouse_comparison.clicked_name', mouse_comparison.clicked_name[0])
            trials_posttest.addData('mouse_comparison.started', mouse_comparison.tStart)
            trials_posttest.addData('mouse_comparison.stopped', mouse_comparison.tStop)
            trials_posttest.addData('stim1_comparison.started', stim1_comparison.tStartRefresh)
            trials_posttest.addData('stim1_comparison.stopped', stim1_comparison.tStopRefresh)
            trials_posttest.addData('stim2_comparison.started', stim2_comparison.tStartRefresh)
            trials_posttest.addData('stim2_comparison.stopped', stim2_comparison.tStopRefresh)
            trials_posttest.addData('stim3_comparison.started', stim3_comparison.tStartRefresh)
            trials_posttest.addData('stim3_comparison.stopped', stim3_comparison.tStopRefresh)
            clickedname=mouse_comparison.clicked_name[0].split('_')[0] 
            # clickedname = "stim1" OR "stim2" OR "stim3"
            # ".split(..." removes suffix from name
            thisExp.addData('clickedname',clickedname)
            # add it to our output data
            
            trialcorrect=clickedname==correctstim
            # trialcorrect = TRUE (1) or FALSE (0)
            # compare the clicked element to the correct stim provided by CueTbl
            thisExp.addData('trialcorrect',trialcorrect)
            # add it to our output data
            
            # update trial counters
            correcttrials+=trialcorrect # (1 or 0)
            totaltrials+=1
            
            # control feedback message
            if trialcorrect:
                msg_feedback=f"Correct! Nice Job! \n You got {str(correcttrials)} out of {str(totaltrials)} correct!"
            else:
                msg_feedback="Try Again!"
             
            accuracy=correcttrials/totaltrials
            # get accuracy to compare against mastery criteria
            
            passedBlock=accuracy>=mastery_criteria
            # passedBlock = TRUE (1) or FALSE (0)
            # if accuracy is over mastery criteria, they passed
            
            thisExp.addData('passedBlock',passedBlock)
            # record whether or not participant passed the block
            
            # control block feedback message
            if passedBlock:
                msg_blockfeedback=f"You passed that block! Nice job!"
                # populate a passed/good message
            else:
                msg_blockfeedback=f"You failed that block! Try Again!"
                # populate a failed/bad message
            
            
            # the Routine "comparison" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_posttest'
        
        
        # ------Prepare to start Routine "block_feedback_posttest"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_blockfeedback_2.setText(msg_blockfeedback)
        # setup some python lists for storing info about the mouse_blockfeedback_2
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        block_feedback_posttestComponents = [text_blockfeedback_2, mouse_blockfeedback_2]
        for thisComponent in block_feedback_posttestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        block_feedback_posttestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "block_feedback_posttest"-------
        while continueRoutine:
            # get current time
            t = block_feedback_posttestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=block_feedback_posttestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blockfeedback_2* updates
            if text_blockfeedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blockfeedback_2.frameNStart = frameN  # exact frame index
                text_blockfeedback_2.tStart = t  # local t and not account for scr refresh
                text_blockfeedback_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blockfeedback_2, 'tStartRefresh')  # time at next scr refresh
                text_blockfeedback_2.setAutoDraw(True)
            # *mouse_blockfeedback_2* updates
            if mouse_blockfeedback_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_blockfeedback_2.frameNStart = frameN  # exact frame index
                mouse_blockfeedback_2.tStart = t  # local t and not account for scr refresh
                mouse_blockfeedback_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_blockfeedback_2, 'tStartRefresh')  # time at next scr refresh
                mouse_blockfeedback_2.status = STARTED
                mouse_blockfeedback_2.mouseClock.reset()
                prevButtonState = mouse_blockfeedback_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_blockfeedback_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_blockfeedback_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_feedback_posttestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "block_feedback_posttest"-------
        for thisComponent in block_feedback_posttestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_posttest.addData('text_blockfeedback_2.started', text_blockfeedback_2.tStartRefresh)
        block_posttest.addData('text_blockfeedback_2.stopped', text_blockfeedback_2.tStopRefresh)
        # store data for block_posttest (TrialHandler)
        x, y = mouse_blockfeedback_2.getPos()
        buttons = mouse_blockfeedback_2.getPressed()
        block_posttest.addData('mouse_blockfeedback_2.x', x)
        block_posttest.addData('mouse_blockfeedback_2.y', y)
        block_posttest.addData('mouse_blockfeedback_2.leftButton', buttons[0])
        block_posttest.addData('mouse_blockfeedback_2.midButton', buttons[1])
        block_posttest.addData('mouse_blockfeedback_2.rightButton', buttons[2])
        block_posttest.addData('mouse_blockfeedback_2.started', mouse_blockfeedback_2.tStart)
        block_posttest.addData('mouse_blockfeedback_2.stopped', mouse_blockfeedback_2.tStop)
        if not passedBlock:
            msg_posttest="You will be reset to the training phase."
            # let participants know they are being reset
            block_posttest.finished=True
            # if the participant FAILS the previous block
            # then this will break us out of the "block posttest" loop
            # and skip whatever post-test tasks there are left
        
        else:
            msg_posttest="You passed! \nThanks for taking this experiment!"
            # friendly exit message for when they pass
        
        # the Routine "block_feedback_posttest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'block_posttest'
    
    
    # ------Prepare to start Routine "check_posttest"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_posttest.setText(msg_posttest)
    # keep track of which components have finished
    check_posttestComponents = [text_posttest]
    for thisComponent in check_posttestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    check_posttestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "check_posttest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = check_posttestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=check_posttestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_posttest* updates
        if text_posttest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_posttest.frameNStart = frameN  # exact frame index
            text_posttest.tStart = t  # local t and not account for scr refresh
            text_posttest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_posttest, 'tStartRefresh')  # time at next scr refresh
            text_posttest.setAutoDraw(True)
        if text_posttest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_posttest.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_posttest.tStop = t  # not accounting for scr refresh
                text_posttest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_posttest, 'tStopRefresh')  # time at next scr refresh
                text_posttest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in check_posttestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "check_posttest"-------
    for thisComponent in check_posttestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if passedBlock:
        repeat_task.finished=True
    # if the participant passes the previous block
    # then this will break us out of the "repeat_block" loop
    # otherwise it will continue to repeat
     
    
    repeat_task.addData('text_posttest.started', text_posttest.tStartRefresh)
    repeat_task.addData('text_posttest.stopped', text_posttest.tStopRefresh)
# completed 50.0 repeats of 'repeat_task'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
