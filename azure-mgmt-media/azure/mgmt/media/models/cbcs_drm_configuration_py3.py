# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CbcsDrmConfiguration(Model):
    """Class to specify drm configurations of CommonEncryptionCbcs scheme in
    Streaming Policy.

    :param fair_play: Fairplay configurations
    :type fair_play:
     ~azure.mgmt.media.models.StreamingPolicyFairPlayConfiguration
    :param play_ready: PlayReady configurations
    :type play_ready:
     ~azure.mgmt.media.models.StreamingPolicyPlayReadyConfiguration
    :param widevine: Widevine configurations
    :type widevine:
     ~azure.mgmt.media.models.StreamingPolicyWidevineConfiguration
    """

    _attribute_map = {
        'fair_play': {'key': 'fairPlay', 'type': 'StreamingPolicyFairPlayConfiguration'},
        'play_ready': {'key': 'playReady', 'type': 'StreamingPolicyPlayReadyConfiguration'},
        'widevine': {'key': 'widevine', 'type': 'StreamingPolicyWidevineConfiguration'},
    }

    def __init__(self, *, fair_play=None, play_ready=None, widevine=None, **kwargs) -> None:
        super(CbcsDrmConfiguration, self).__init__(**kwargs)
        self.fair_play = fair_play
        self.play_ready = play_ready
        self.widevine = widevine
