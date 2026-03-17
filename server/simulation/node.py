class Node:
  def __init__(self, name, inv, reorder_point, order_quantity, lead_time):
    self.name = name
    self.inv = inv
    self.reorder_point = reorder_point
    self.order_quantity = order_quantity
    self.lead_time = lead_time

    self.pending_orders = []
    self.stockouts = 0
    self.inventory_history = []
  