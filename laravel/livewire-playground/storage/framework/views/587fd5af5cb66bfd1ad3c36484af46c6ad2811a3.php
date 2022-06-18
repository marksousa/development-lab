<div>
    <input wire:model="nome" type="text">
    <input wire:model="isHuman" type="checkbox">
    <input wire:model="gender" value="Male" type="radio">
    <input wire:model="gender" value="Female" type="radio">
    Hello <?php echo e($nome); ?>! Gender: <?php echo e($gender); ?>

    <?php if($isHuman): ?>
        <p>You're an human!</p>
    <?php endif; ?>

</div>
<?php /**PATH /home/mark/workspace/study/development-lab/laravel/livewire-playground/resources/views/livewire/hello-world.blade.php ENDPATH**/ ?>