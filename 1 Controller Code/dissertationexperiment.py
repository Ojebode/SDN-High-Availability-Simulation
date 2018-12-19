#!/usr/bin/python

"""
This script was written for a dissertation experiment at Edge Hill 
Univeristy to create an SDN network topology with a remote controller .
"""

#Import modules from packages
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

# Create empty network
def emptyNetwork():

    "Add nodes to network and call a remote controller."

# Define which controller to be used by Mininet, In this case a remote controller
    network = Mininet( controller=RemoteController )

# Add a controller to the network by specifying the IP address and port number of the remote controller
    info( '*** Adding/connecting to remote controller\n' )
    network.addController( 'c0' , controller=RemoteController,ip="192.168.63.52",port=6633)

# Add hosts to the network with a specified IP address
    info( '*** Joining four hosts to network\n' )
    lSH1 = network.addHost( 'h1', ip='50.0.0.1' )
    lSH2 = network.addHost( 'h2', ip='50.0.0.2' )
    rSH1 = network.addHost( 'h3', ip='50.0.0.1' )
    rSH2 = network.addHost( 'h4', ip='50.0.0.2' )

# Define variables to Add switches to the network
    info( '*** Joining three switches to network\n' )
    topSwitch = network.addSwitch( 's1' )
    leftSwitch = network.addSwitch( 's2' )
    rightSwitch = network.addSwitch( 's3' )
    
# Add links to connect switches and hosts
    info( '*** Creating links between Hosts and Switches\n' )
    network.addLink( topSwitch, leftSwitch )
    network.addLink( topSwitch, rightSwitch )
    leftSwitchHost = (lSH1,lSH2)
    rightSwitchHost = (rSH1,rSH2)

    for array in range( 0, len(leftSwitchHost)):
        network.addLink(leftSwitchHost[array], leftSwitch)

    for array2 in range( 0, len(rightSwitchHost)):
        network.addLink(rightSwitchHost[array2], rightSwitch)

# System Log to display that network is starting and method to launch Mininet
    info( '*** Starting network\n')
    network.start()

# Method to present a command line prompt
    info( '*** Running CLI\n' )
    CLI( network )

# Method to stop network when exit command is issued
    info( '*** Stopping network' )
    network.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNetwork()
