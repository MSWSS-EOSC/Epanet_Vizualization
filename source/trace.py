"""
The following example demonstrates how to import WNTR, generate a water network 
model from an INP file, simulate hydraulics, and plot simulation results on the network.
"""
import wntr
import os
import sys
from matplotlib import animation

# Create a water network model
inp_file = 'Bratislava-new.inp'
inp_file = sys.argv[1]
wn = wntr.network.WaterNetworkModel(inp_file)
#
# fig, ax = plt.subplots(1, 1, figsize=(12, 4))
#
# # Graph the network
# wntr.graphics.plot_network(wn, title=wn.name)
#
# # Simulate hydraulics
# sim = wntr.sim.EpanetSimulator(wn)
# results = sim.run_sim()

# # Plot results on the network
# pressure_at_5hr = results.node['pressure'].loc[5*3600, :]
# flow_at_5hr = results.link['flowrate'].loc[5*3600, :]*1000
# wntr.graphics.plot_network(wn, node_attribute=pressure_at_5hr, node_size=30,
#                        title='Pressure at 5 hours')
#
# Fig, Axarr = plt.subplots(1, 2, figsize=(240, 80))
# Ax0 = Axarr[0]
# wntr.graphics.plot_network(wn,
#                            node_attribute=pressure_at_5hr,
#                            node_size=30, node_range=[0, 50],
#                            title='Pressure',
#                            node_colorbar_label='Pressure (bar)', ax=Ax0)
#
# Ax1 = Axarr[1]
# wntr.graphics.plot_network(wn,
#                            link_attribute=flow_at_5hr,
#                            node_size=10, link_width=3, link_range=[0, 100],
#                            title='Flow',
#                            link_colorbar_label='Flow (l/s)', filename='a.png', ax=Ax1)
#
# wntr.graphics.plot_interactive_network(wn,
#                                        node_attribute=pressure_at_5hr,
#                                        node_size=30, node_range=[0, 50],
#                                        figsize=[70000, 45000],
#                                        title='Pressure', auto_open=False, filename='a.html')
#
# wntr.graphics.plot_interactive_network(wn,
#                            link_attribute=flow_at_5hr,
#                            node_size=10,link_width=3, link_range= [0,100],
#                            title='Flow',
#                            link_colorbar_label='Flow (l/s)', filename='a.html', ax=Ax1)

# longlat_map = {'1_1000':(17.10323576392309, 48.17509565209662), '1_12317': (17.20115845631565, 48.12497796949683)}
#
# longlat_map = {'46':(17.03894710696975, 48.31234273447002), '8': (17.08601837714516, 48.134740154588734)}
#
# wn2 = wntr.morph.convert_node_coordinates_to_longlat(wn, longlat_map)
#
# fig, ax = plt.subplots(1, 1, figsize=(12, 4))
#
# # Graph the network
# wntr.graphics.plot_network(wn2, title=wn.name)
#
# # Simulate hydraulics
# sim = wntr.sim.EpanetSimulator(wn2)
# results = sim.run_sim()
#
# # Plot results on the network
# pressure_at_7hr = results.node['pressure'].loc[7*3600, :]
# flow_at_7hr = results.link['flowrate'].loc[7*3600, :]*1000
#
# # length = wn2.query_link_attribute('length')
# # wntr.graphics.plot_leaflet_network(wn2, link_attribute=length, link_width=3,
# #                                     link_range=[0,1000], filename='length.html', )
#
# wntr.graphics.plot_leaflet_network(wn2,
#                                    link_attribute_name='Flow at 7hr',
#                                    link_attribute=flow_at_7hr,
#                                    link_range=[0, None],
#                                    link_width=3,
#                                    link_cmap=['blue', 'blueviolet', 'cornflowerblue', 'forestgreen', 'greenyellow', 'gold', 'orange', 'firebrick'],
#                                    link_labels=True,
#                                    node_attribute_name='Pressure at 7hr',
#                                    node_attribute=pressure_at_7hr,
#                                    node_cmap=['blue', 'blueviolet', 'cornflowerblue', 'forestgreen', 'greenyellow', 'gold', 'orange', 'firebrick'],
#                                    node_size=10, node_range=[0, None],
#                                    node_labels=True,
#                                    add_legend=True, filename='Bratislava.html', round_ndigits=0)


wn.options.quality.parameter = 'AGE'
wn.options.quality.parameter = 'CHEMICAL'
wn.options.time.hydraulic_timestep = 60*60
wn.options.time.quality_timestep = 60*60
wn.options.time.report_timestep = 60*60
wn.options.quality.parameter = 'TRACE'
# wn.options.quality.trace_node = '157'
# wn.options.quality.trace_node = '9'
wn.options.quality.trace_node = sys.argv[2]
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim()

water_flow = results.node['quality']/(60*60) # convert seconds to hours
anim = wntr.graphics.network_animation(wn, node_attribute=water_flow, node_range=[None, None], repeat=False,
                                       title='Spreading toxins from node: ' + sys.argv[2])
# anim.save(filename='Bratislava-new.gif')
writergif = animation.PillowWriter(fps=5)
# writervideo = animation.FFMpegWriter(fps=60)
anim.save(filename=sys.argv[3] + '.gif', writer=writergif, dpi=300)
# anim.save(filename=sys.argv[3], writer=writergif, **format='gif')
os.replace(sys.argv[3] + '.gif', sys.argv[3])

