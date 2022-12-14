#*
# * Decorates another {@link FieldMapper} to record its timing.
# * <p>
# * Parameters of metric can be customized via {@link MeteringFieldMapperDecorator#metricTimerFactory}.
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * P - Type of parameters object.
# 


class MeteringFieldMapperDecorator(GroovyObjectSupport, FieldMapper):
    #    *
    #     * Creates instance.
    #     *
    #     :param delegate:             Mapper to be metered.
    #     :param metricRegistry:       Registry where to report metrics to.
    #     :param metricNameCalculator: Calculator for metric name.
    #     


    def __init__(self, delegate, metricRegistry, metricNameCalculator):
        self.delegate = delegate
        self.metricRegistry = metricRegistry
        self.metricNameCalculator = metricNameCalculator




    def mapField(self, field, mappingContext):
        metricName = metricNameCalculator.calculateMetricName(field, mappingContext)
        metricRegistry.invokeMethod("timer", [metricName, getMetricTimerFactory()]).invokeMethod("time", [RunnableAnonymousInnerClass(self, field, mappingContext)])

    class RunnableAnonymousInnerClass(Runnable):


        def __init__(self, outerInstance, field, mappingContext):
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext

        def run(self):
            delegate.mapField(self._field, self._mappingContext)


    def getMetricTimerFactory(self):
        return metricTimerFactory

    def setMetricTimerFactory(self, metricTimerFactory):
        self.metricTimerFactory = metricTimerFactory

    #    *
    #     * Factory that is to be used to create timer metrics.
    #     * <p>
    #     * By default, uses default parameters of {@link com.codahale.metrics.Timer#Timer()}.
    #     

    #    *
    #     * Calculates metric name.
    #     * <p>
    #     * OO - Original object type.
    #     * RO - Resulting object type.
    #     * P - Type of parameters object.
    #     
    class MetricNameCalculator(GroovyObjectSupport):
        #        *
        #         * Calculates name of the metric.
        #         *
        #         :param field:          Field that is being mapped.
        #         :param mappingContext: Mapping context.
        #         * @return Name of the metric that should track mapping time of delegate.
        #         


        def calculateMetricName(self, field, mappingContext):
            pass

        class MetricSupplierAnonymousInnerClass(MetricRegistry.MetricSupplier):
            def newMetric(self):
                return Timer()

