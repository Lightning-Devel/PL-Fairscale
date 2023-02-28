# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Optional, Union

from fairscale.optim import OSS
from fairscale.optim.grad_scaler import ShardedGradScaler
from pytorch_lightning.plugins.precision.native_amp import MixedPrecisionPlugin
from typing_extensions import Literal


class ShardedMixedPrecisionPlugin(MixedPrecisionPlugin):
    """Native AMP for Sharded Training."""

    def __init__(
        self, precision: Literal["16", 16, "bf16"], device: str, scaler: Optional[ShardedGradScaler] = None
    ) -> None:
        super().__init__(
            precision, device, scaler=(ShardedGradScaler() if scaler is None and str(precision) == "16" else None)
        )

    def clip_grad_by_norm(self, optimizer: "OSS", clip_val: Union[int, float]) -> None:
        optimizer.clip_grad_norm(clip_val)
