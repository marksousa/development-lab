<?php $__env->startSection('content'); ?>
    <?php
if (! isset($_instance)) {
    $html = \Livewire\Livewire::mount('register')->html();
} elseif ($_instance->childHasBeenRendered('WacSVEG')) {
    $componentId = $_instance->getRenderedChildComponentId('WacSVEG');
    $componentTag = $_instance->getRenderedChildComponentTagName('WacSVEG');
    $html = \Livewire\Livewire::dummyMount($componentId, $componentTag);
    $_instance->preserveRenderedChild('WacSVEG');
} else {
    $response = \Livewire\Livewire::mount('register');
    $html = $response->html();
    $_instance->logRenderedChild('WacSVEG', $response->id(), \Livewire\Livewire::getRootElementTagName($html));
}
echo $html;
?>
<?php $__env->stopSection(); ?>
<?php echo $__env->make('layouts.app', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH /home/mark/workspace/study/development-lab/laravel/livewire-playground/resources/views/register.blade.php ENDPATH**/ ?>